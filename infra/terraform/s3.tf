# S3 bucket for artifacts and optional terraform state
resource "aws_s3_bucket" "artifacts" {
  bucket = "${var.resource_prefix}-artifacts"
  acl    = "private"
  tags = {
    Name = "${var.resource_prefix}-artifacts"
  }
}
