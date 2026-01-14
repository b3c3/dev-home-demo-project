import sys
import os
import subprocess

def upload_file(bucket_name, file_path):
    """
    Uploads a file to an S3 bucket using the AWS CLI.
    """
    # 1. Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return False

    # 2. Check if bucket exists (or at least is accessible)
    print(f"Checking if bucket '{bucket_name}' exists...")
    try:
        subprocess.run(
            ["aws", "s3", "ls", f"s3://{bucket_name}"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError:
        print(f"Error: The bucket '{bucket_name}' does not exist or you do not have permission to access it.")
        return False

    # 3. Upload the file to the S3 bucket
    print(f"Uploading '{file_path}' to s3://{bucket_name}...")
    try:
        subprocess.run(
            ["aws", "s3", "cp", file_path, f"s3://{bucket_name}/"],
            check=True
        )
        print("Success! File uploaded successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print("Error: The S3 upload failed.")
        return False


if __name__ == "__main__":
    # 0. Check arguments
    if len(sys.argv) != 3:
        print("Error: [Invalid number of arguments] ")
        print("You have not provided the required arguments to execute the script.")
        print("Usage: python3 upload_file.py <bucket_name> <file_path>")
        sys.exit(1)

    bucket = sys.argv[1]
    file = sys.argv[2]

    if not upload_file(bucket, file):
        sys.exit(1)

# End of file