# Infra README

Este diretório contém arquivos Terraform de exemplo para provisionar recursos na AWS (us-east-1) usados pelo POC CYBER-IA.

Recursos criados (exemplos):
- S3 bucket para artifacts/state
- DynamoDB table para locking do Terraform
- KMS key (com alias)
- RDS Postgres (exemplo)

ATENÇÃO: Estes arquivos são apenas um ponto de partida. Eles NÃO devem ser aplicados sem revisão.

Passos sugeridos:
1) Configure suas credenciais AWS (AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY) com permissões para criar S3, DynamoDB, KMS, RDS.
2) Inicialize o Terraform: terraform init
3) Revise o plano: terraform plan
4) Aplique: terraform apply

Recomendações de segurança:
- Use backend remoto para o estado (S3 + DynamoDB) antes de colaborar
- Restrinja políticas IAM e políticas de KMS
- Configure backups e Multi-AZ para RDS em produção
