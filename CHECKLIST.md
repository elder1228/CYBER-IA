# CHECKLIST de Segurança & Deploy

Antes de aplicar infra / deploy
- [ ] Revisar arquivos Terraform e variáveis
- [ ] Configurar backend remoto do Terraform (S3 + DynamoDB)
- [ ] Criar e armazenar secrets em GitHub Secrets
- [ ] Revisar políticas IAM e limitar permissões

Após deploy
- [ ] Habilitar logging e auditoria (CloudTrail, S3 access logs)
- [ ] Configurar backups e snapshots para RDS
- [ ] Configurar monitoramento e alertas
- [ ] Revisão de segurança / pentest
