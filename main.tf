variable "learner_name" {
  description = "The name of the learner to be used as the bucket prefix. No spaces or special characters."
  type        = string
}

provider "aws" {
  region = "us-east-1"
  # SECURITY NOTE: Never hardcode credentials in your .tf files!
  # Terraform can pick up credentials from:
  # 1. Environment Variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
  # 2. AWS Shared Credentials File (~/.aws/credentials)
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "unique_bucket" {
  # Bucket naming rules: Lowercase, numbers, hyphens.
  # We combine the learner name with a random suffix for uniqueness.
  bucket = "${lower(var.learner_name)}-${random_id.bucket_suffix.hex}"

  tags = {
    Name        = "Unique S3 Bucket for ${var.learner_name}"
    Environment = "CIL Academy Sandbox"
    Owner       = var.learner_name
  }
}

output "bucket_name" {
  value       = aws_s3_bucket.unique_bucket.id
  description = "The unique name of the S3 bucket created"
}
