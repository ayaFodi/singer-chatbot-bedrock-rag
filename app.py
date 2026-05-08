from flask import Flask, jsonify, render_template, request
import boto3
from botocore.exceptions import ClientError, NoCredentialsError
import os

REGION = os.getenv("AWS_REGION", "us-east-1")
AGENT_ID = os.getenv("BEDROCK_AGENT_ID")
AGENT_ALIAS_ID = os.getenv("BEDROCK_AGENT_ALIAS_ID")

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")


def invoke_bedrock_agent(prompt: str) -> str:
    client = boto3.client("bedrock-agent-runtime", region_name=REGION)
    session_id = "12"

    try:
        response = client.invoke_agent(
            agentId=AGENT_ID,
            agentAliasId=AGENT_ALIAS_ID,
            sessionId=session_id,
            inputText=prompt
        )

        output_parts = []
        for event in response.get("completion", []):
            chunk = event.get("chunk")
            if chunk and "bytes" in chunk:
                output_parts.append(chunk["bytes"].decode("utf-8"))

        return "".join(output_parts) or "No answer returned."

    except NoCredentialsError:
        return "AWS credentials were not found."
    except ClientError as e:
        return f"AWS error: {e.response['Error']['Message']}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@app.route('/ask', methods=['POST'])
def ask():
    payload = request.get_json(silent=True) or {}
    message = (payload.get("message") or "").strip()

    if not message:
        return jsonify({"answer": "Please provide a message."}), 400



    answer = invoke_bedrock_agent(message)
    return jsonify({"answer": answer})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)