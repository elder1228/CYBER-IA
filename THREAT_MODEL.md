# THREAT MODEL (Resumo)

Ativos principais
- Chaves criptográficas (KMS/HSM)
- Dados sensíveis cifrados (arquivos, logs)
- Pipelines de ML/IA usados para análise
- Infraestrutura de cloud (RDS, S3)

Principais ameaças
- Comprometimento de chaves: proteger com KMS/HSM, rotação e least-privilege
- Vazamento de dados via IA: remover PII antes de enviar para modelos externos
- Configuração incorreta de infra (S3 público, RDS público)
- Supply chain: dependências maliciosas

Mitigações
- KMS + policies, uso de HSM em produção
- Mascaramento/anonimização de logs antes de enviar para LLMs
- Scanning de dependências (SCA), SBOM e revisão de CI
- Logging imutável e auditoria (WORM storage, S3 Object Lock)
