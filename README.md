# Mini-Project to Demonstrate using the Dev-Home & Dev-Tools Setup

Welcome!   
This mini-project demonstrates how to use the tools set up in the CIL Academy Guide Document - "_How to Setup Your Dev-Home Folder_".       

You will use Terraform to provision a unique AWS S3 bucket and then verify it by uploading a file using a Python script (which uses AWS CLI S3 commands to do the job).

Clone this repository into your Dev-Projects folder and then either follow the trainer's instructions (where applicable) or use the guide below to complete it.

## Project Goal & Tools

- **Goal**: Create an S3 bucket in AWS and verify write access.
- **Tools**: Git, Terraform, AWS CLI, Python.

## Prerequisites

- Terraform installed
- AWS Account access
- Python 3 installed (for the verification script)

## 1. Setting up Credentials (IMPORTANT)

To allow Terraform to create resources in AWS, it needs your credentials. **Never share these keys or commit them to GitHub!**

### Option 1: Environment Variables (Recommended for Shared Computers)
Run these commands in your terminal before running Terraform:

#### macOS / Linux / Cloud Shell
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
1. Run `aws configure`
2. Enter your **Access Key ID** and **Secret Access Key**.
3. Default region: `us-east-1`
4. Default output: `json`

---

## 2. Infrastructure Deployment (Terraform)

1.  **Initialize the project** (downloads the AWS provider):
    ```bash
    terraform init
    ```

2.  **Plan the changes** (replace `yourname` with your actual name):
    ```bash
    terraform plan -var="learner_name=yourname"
    ```

3.  **Apply the changes** to create the bucket:
    ```bash
    terraform apply -var="learner_name=yourname"
    ```
    *Type `yes` when prompted to confirm.*

    **Note**: After a successful apply, Terraform will output the `bucket_name`. Copy this name for the next steps!

---

## 3. Verification & Testing

Now that the infrastructure is created, let's verify it works.

### Step A: Verify Bucket Creation
Check if your bucket is listed in your AWS account:
```bash
aws s3 ls | grep yourname
```

### Step B: Test File Upload
We have provided a Python script `upload_file.py` to test uploading a file to your new bucket.

We have also provided a sample image you can use for testing (`lab-resources/secret.png`). Do feel free to create or use your own file (e.g., as seen below).


1.  Create a test file:
    ```bash
    echo "Hello, S3!" > test_file.txt
    ```

2.  Run the upload script:
    
    ```bash
    python3 upload_file.py <bucket_name> test_file.txt
    ```
    - *Replace `<bucket_name>` with the output from the terraform apply step.*

    If using the sample image provided in the lab_resources folder, the command should be:
    ```bash
    python3 upload_file.py <bucket_name> lab-resources/secret.png
    ```
     - *Replace `<bucket_name>` with the output from the terraform apply step.*

    You can upload as many files as you wish, just specify their path.


3.  If successful, you will see:
    > Success! File uploaded successfully.

---

## 4. Cleanup

When finished, you **MUST empty the bucket** before destroying the infrastructure. Terraform cannot destroy a non-empty bucket by default.

1.  Empty the bucket:
    ```bash
    aws s3 rm s3://<bucket_name> --recursive
    ```
    - *Replace `<bucket_name>` with the output from the terraform apply step.*

2.  Destroy the resources:
    ```bash
    terraform destroy -var="learner_name=yourname"
    ```
    *Type `yes` to confirm.*

## Conclusion

Congratulations! You have successfully used Terraform to provision an AWS S3 bucket, verified it with a custom Python script, and cleaned up your resources. This workflow demonstrates the core cycle of Infrastructure as Code: Init -> Plan -> Apply -> Verify -> Destroy.
