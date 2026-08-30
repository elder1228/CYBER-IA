# RDS Postgres instance (basic example). Customize to your needs.
resource "aws_db_subnet_group" "default" {
  name       = "${var.resource_prefix}-subnet-group"
  subnet_ids = [] # provide subnet ids in variables or create new subnets
  tags = {
    Name = "${var.resource_prefix}-subnet-group"
  }
}

resource "aws_db_instance" "postgres" {
  identifier              = "${var.resource_prefix}-db"
  allocated_storage       = 20
  engine                  = "postgres"
  engine_version          = "15"
  instance_class          = "db.t3.micro"
  name                    = "cyberia"
  username                = var.db_username
  password                = var.db_password
  skip_final_snapshot     = true
  publicly_accessible     = false
  db_subnet_group_name    = aws_db_subnet_group.default.name
  # security_groups         = [aws_security_group.rds_sg.id]

  tags = {
    Name = "${var.resource_prefix}-rds"
  }
}
