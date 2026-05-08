# Singer Chatbot – AWS Bedrock RAG Application

## 📌 Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot application that answers questions about famous Arabic singers using an AI agent built with Amazon Bedrock.

The project was developed as part of a NorthMed course in collaboration with Deloitte and demonstrates the integration of AWS AI services with a Flask web application deployed on cloud infrastructure.

---

## 🎤 Knowledge Base Content

The chatbot uses a custom Knowledge Base containing documents about well-known Arabic singers, including:

- Fairuz
- Umm Kulthum
- Wadi’ Al-Safi
- Sabah Fakhri
- George Wassouf

These documents were uploaded to Amazon S3 and connected to the Bedrock Knowledge Base to provide grounded and factual responses.

---

## ⚙️ System Architecture

### Application Flow

1. The user enters a question through the chatbot web interface.
2. A Flask backend receives the request.
3. The backend sends the query to an Amazon Bedrock Agent.
4. The Bedrock Agent retrieves relevant information from the Knowledge Base.
5. The generated response is returned and displayed to the user.

The application was containerized using Docker and deployed on an AWS EC2 instance for testing.

---

## 🧠 Features

- RAG-based question answering
- Context-aware conversations
- Knowledge Base grounded responses
- Flask web interface
- AWS Bedrock Agent integration
- Docker containerization
- AWS EC2 cloud deployment

---

## ☁️ AWS Services Used

- Amazon Bedrock Agent
- Amazon Bedrock Knowledge Base
- Amazon S3
- Amazon OpenSearch
- Amazon EC2
- AWS IAM

---

## 🐳 Deployment

The Flask application was containerized using Docker and executed inside a Docker container on an AWS EC2 instance.

### Docker Commands

```bash
docker build -t singers_flask_app .
docker run -p 5000:5000 singers_flask_app
```

## 🔐 Environment Variables

Before running the application, configure the following environment variables:

```bash
export AWS_REGION=us-east-1
export BEDROCK_AGENT_ID=your_agent_id
export BEDROCK_AGENT_ALIAS_ID=your_alias_id
```

---

## ▶️ Running the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open in browser:

```text
http://localhost:5000
```

---

## 📷 Project Documentation

The project documentation includes:

- Chatbot UI screenshots
- Mobile public access testing
- Conversation examples
- Amazon Bedrock Agent configuration
- Knowledge Base setup
- Docker deployment
- Docker Hub repository
- AWS EC2 hosting
- Security group configuration

---

## 🧹 Resource Cleanup

To avoid unnecessary AWS charges, all cloud resources were deleted after testing:

- EC2 instance terminated
- OpenSearch resources deleted
- Docker containers stopped
- No active AWS services remain running

---

## 🧠 Summary

This project demonstrates how to integrate a custom Amazon Bedrock AI agent with a Flask web application using Retrieval-Augmented Generation (RAG) architecture and deploy it on AWS cloud infrastructure using Docker and EC2.