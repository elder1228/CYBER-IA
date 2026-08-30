Objetivo
- Incluir templates Terraform para AWS us-east-1: KMS, RDS (Postgres), S3 bucket, DynamoDB para locking; provider/variables/outputs e README explicativo.

O que contém este PR
- infra/terraform/provider.tf  
- infra/terraform/variables.tf  
- infra/terraform/s3.tf  
- infra/terraform/backend.tf (DynamoDB lock)  
- infra/terraform/kms.tf  
- infra/terraform/rds.tf  
- infra/terraform/outputs.tf  
- infra/terraform/README.md

Como revisar / testar (IMPORTANTE)
- Estes arquivos são templates. NÃO aplicar sem revisão.  
- Passos sugeridos:
  1) Configure credenciais AWS com permissões mínimas necessárias  
  2) Revisar nomes de bucket/tabela para evitar conflito  
  3) Criar backend S3/DynamoDB manualmente ou ajustar backend e inicializar terraform  
  4) terraform init → terraform plan → revisar custos → terraform apply (aplicar somente se estiver de acordo)

Checklist de revisão
- [ ] Revisar variáveis sensíveis (db_password etc.)  
- [ ] Confirmar nomes de bucket e tabela DynamoDB  
- [ ] Executar terraform plan e revisar custos estimados  
- [ ] Verificar políticas IAM e KMS key policies

Avisos de custo e segurança
- RDS, KMS e S3 criam custos. Configure tags e orçamento.  
- Habilite rotação de chave KMS e restrinja key policy.  
- Não aplicar em produção sem planejamento de rede (VPC/subnets/security groups).