# DynamoDB table for Terraform state locking
resource "aws_dynamodb_table" "terraform_lock" {
  name         = "${var.resource_prefix}-terraform-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Name = "${var.resource_prefix}-terraform-lock"
  }
}
