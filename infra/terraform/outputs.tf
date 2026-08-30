output "s3_bucket" {
  value = aws_s3_bucket.artifacts.bucket
}

output "dynamodb_table" {
  value = aws_dynamodb_table.terraform_lock.name
}

output "kms_key_id" {
  value = aws_kms_key.cyber_key.key_id
}

output "rds_endpoint" {
  value = aws_db_instance.postgres.endpoint
}
