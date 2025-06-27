# 🚀 Serverless Framework Hello API (AWS Python HTTP API)

This project demonstrates a simple `hello world` API using the **Serverless Framework** on AWS. It uses **Python** as the runtime and **HTTP API Gateway** to expose a basic endpoint. The setup is done from scratch on an **EC2 instance** (acting as a development headquarters).

---

## 🧰 Prerequisites

Make sure you have the following set up on your EC2 instance:

- ✅ Node.js and npm
- ✅ Python 3.x
- ✅ AWS CLI
- ✅ Serverless Framework

---

## ⚙️ Initial Setup

### 1. Launch EC2 Instance (Headquarter)

- Create and connect to a new EC2 instance (Amazon Linux 2 or Ubuntu).
- Update packages:

  ```bash
  sudo apt update    
  ```
  ![Ec2](https://github.com/AmanSharma39/aws-python-http-api/blob/main/images/Screenshot%202025-06-27%20083025.png?raw=true)
###  2. Install Node.js & npm
Install Node.js (if not already installed):
```bash
sudo apt install nodejs npm  
```

Update npm and install Serverless globally:
```bash 
npm install -g npm
sudo npm install -g serverless
```
### 🧪 Create Hello API Project

Run the following Serverless command to scaffold a new Python-based HTTP API project:
```bash
serverless create --template aws-python-http-api --path hello-api
cd hello-api
```
Project structure:
```bash
hello-api/
│
├── handler.py         # Python Lambda function
└── serverless.yml     # Infrastructure as Code (IaC)
```
* handler.py

  ![handler](https://github.com/AmanSharma39/aws-python-http-api/blob/main/images/Screenshot%202025-06-27%20094650.png?raw=true)

* serverless.yml

  ![serverless](https://github.com/AmanSharma39/aws-python-http-api/blob/main/images/Screenshot%202025-06-27%20111714.png?raw=true)

You can customize your `handler.py` to define your logic, for example:
```bash
import json


def hello(event, context):
    body = {
        "message": "Hello jiiii",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
```
## 🔐 Set Up AWS Credentials

### 1. Create an IAM user
* Go to AWS Console → IAM → Users → Add User
* Programmatic access → Attach AdministratorAccess (for learning/demo)

### 2. Install AWS CLI:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
 ![Alt text](https://github.com/AmanSharma39/aws-python-http-api/blob/main/images/Screenshot%202025-06-27%20091354.png?raw=true)

Configure with your IAM user credentials:
```bash
aws configure
```

Provide:
- AWS Access Key ID
- AWS Secret Access Key
- Region (e.g., `us-east-1`)
- Output format (e.g., json)

![Access key](https://github.com/AmanSharma39/aws-python-http-api/blob/main/images/Screenshot%202025-06-27%20091048.png?raw=true)

![Secret key](https://github.com/AmanSharma39/aws-python-http-api/blob/main/images/Screenshot%202025-06-27%20091459.png?raw=true)

## 🚀 Deploy to AWS
From within your project directory:
```bash
serverless deploy
```
![deploy](https://github.com/AmanSharma39/aws-python-http-api/blob/main/images/Screenshot%202025-06-27%20094335.png?raw=true)

You'll get an output like:
```bash
endpoints:
  GET - https://xyz123.execute-api.us-east-1.amazonaws.com/
functions:
  hello: hello-api-dev-hello
```
![deploy](https://github.com/AmanSharma39/aws-python-http-api/blob/main/images/Screenshot%202025-06-27%20094627.png?raw=true)

Test it in the browser or via `curl`.

## 🧹 Clean Up
```bash
serverless remove
```
