# Terraform S3 Bucket Lab

Welcome! In this lab, you will create your own unique S3 bucket using Terraform.

## Prerequisites

- Terraform installed
- AWS Account access

## 1. Setting up Credentials (IMPORTANT)

To allow Terraform to create resources in AWS, it needs your credentials. **Never share these keys or commit them to GitHub!**

There are two main ways to provide these credentials. Choose the one that works best for you.

### Option 1: Environment Variables (Recommended for Shared Computers)
This method keeps credentials out of your files completely. They disappear when you close the terminal.

#### macOS / Linux / Cloud Shell
Run these commands in your terminal before running Terraform:

```bash
export AWS_ACCESS_KEY_ID="your_access_key_id_here"
export AWS_SECRET_ACCESS_KEY="your_secret_access_key_here"
# Optional: Set session token if using temporary credentials
# export AWS_SESSION_TOKEN="your_session_token_here"
```

#### Windows (PowerShell)
```powershell
$Env:AWS_ACCESS_KEY_ID="your_access_key_id_here"
$Env:AWS_SECRET_ACCESS_KEY="your_secret_access_key_here"
```

### Option 2: AWS CLI Configure (Persistent)
If you have the AWS CLI installed, you can save your credentials permanently so you don't have to type them every time.

1. Open your terminal.
2. Run:
   ```bash
   aws configure
   ```
3. Paste your **Access Key ID** and **Secret Access Key** when prompted.
4. Set default region name to `us-east-1` (or your preferred region).
5. Set default output format to `json` (optional).

*Note: This saves credentials to a file on your computer (`~/.aws/credentials`). Use this only on your own personal machine.*


## 2. Running Terraform

Initialize the project (downloads the AWS provider):
```bash
terraform init
```

Plan the changes (replace `yourname` with your actual name):
```bash
terraform plan -var="student_name=yourname"
```

Apply the changes to create the bucket:
```bash
terraform apply -var="student_name=yourname"
```

When finished, destroy the resources so you don't incur costs:
```bash
terraform destroy -var="student_name=yourname"
```
