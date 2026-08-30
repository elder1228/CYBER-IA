variable "aws_region" {
  description = "AWS region to create resources in"
  type = string
  default = "us-east-1"
}

variable "resource_prefix" {
  description = "Prefix used for naming resources"
  type = string
  default = "cyber-ia-elder1228"
}

variable "vpc_id" {
  description = "(Optional) VPC id where to create RDS. If empty, RDS will be created in default VPC"
  type = string
  default = ""
}

variable "db_username" {
  description = "Database master username"
  type = string
  default = "cyberia"
}

variable "db_password" {
  description = "Database master password"
  type = string
  default = "changeme"
}
