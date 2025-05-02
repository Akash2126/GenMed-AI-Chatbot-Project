# 🧠 GenMed AI Chatbot Project


This project is a complete pipeline of a medical chatbot using OpenAI and Pinecone vector DB with LangChain, built using Python and Flask.

## 🔧 How to Run?

### 🔁 Step 1: Clone the Repository

```bash
git clone https://github.com/Akash2126/GenMed-AI-Chatbot-Project.git
cd GenMed-AI-Chatbot-Project

🐍 Step 2: Create and Activate Conda Environment
bash
Copy
Edit
conda create -n medibot python=3.10 -y
conda activate medibot
📦 Step 3: Install the Requirements
bash
Copy
Edit
pip install -r requirements.txt
🔐 Step 4: Add API Keys
Create a .env file in the root directory and add the following credentials:

ini
Copy
Edit
PINECONE_API_KEY = "your_pinecone_api_key"
OPENAI_API_KEY = "your_openai_api_key"
🧠 Step 5: Store Embeddings
bash
Copy
Edit
python store_index.py
🚀 Step 6: Run the App
bash
Copy
Edit
python app.py
Now, open your browser and go to:

bash
Copy
Edit
localhost:5000
🛠️ Tech Stack Used
Python

LangChain

Flask

OpenAI GPT

Pinecone

🚀 AWS CICD Deployment with GitHub Actions
✅ Step 1: Login to AWS Console
✅ Step 2: Create IAM User with Permissions
Access Types:
EC2: For launching virtual machines

ECR: For storing docker images

Required Policies:
AmazonEC2ContainerRegistryFullAccess

AmazonEC2FullAccess

✅ Step 3: Create an ECR Repository
Example:
970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot

✅ Step 4: Launch EC2 Instance (Ubuntu)
✅ Step 5: Install Docker on EC2
bash
Copy
Edit
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
✅ Step 6: Configure EC2 as a Self-Hosted Runner
Go to your GitHub repo
→ Settings → Actions → Runners → Add New → Choose OS (Ubuntu) → Run setup commands in EC2 terminal

✅ Step 7: Set GitHub Secrets

Key	Description
AWS_ACCESS_KEY_ID	IAM Access Key
AWS_SECRET_ACCESS_KEY	IAM Secret Key
AWS_DEFAULT_REGION	Example: ap-south-1
ECR_REPO	Your ECR URL
PINECONE_API_KEY	Pinecone API
OPENAI_API_KEY	OpenAI API

![Project UI](https://github.com/username/repository/blob/main/images/Screenshot%202025-05-02%20102434.png)





