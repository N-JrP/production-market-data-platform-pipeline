# Terraform configuration for cloud-style storage (S3 simulation)

provider "aws" {
  region = "eu-central-1"
}

resource "aws_s3_bucket" "market_data_bucket" {
  bucket = "market-data-pipeline-demo-bucket"

  tags = {
    Name        = "Market Data Pipeline"
    Environment = "Demo"
  }
}