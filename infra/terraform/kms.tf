# KMS key for envelope encryption
resource "aws_kms_key" "cyber_key" {
  description             = "KMS key for CYBER-IA POC"
  deletion_window_in_days = 30
  enable_key_rotation     = true

  tags = {
    Name = "${var.resource_prefix}-kms"
  }
}

resource "aws_kms_alias" "cyber_alias" {
  name          = "alias/${var.resource_prefix}-kms"
  target_key_id = aws_kms_key.cyber_key.key_id
}
