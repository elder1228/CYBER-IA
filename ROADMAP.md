# ROADMAP

Fases e entregáveis (curto prazo - 3 meses)

MVP (0-4 semanas)
- Endpoints Encrypt/Decrypt, Generate Key
- Dashboard Web para cifrar/decifrar, upload de logs, chat IA (POC)
- Pipeline simples de detecção de anomalias (IsolationForest)
- Docker Compose para desenvolvimento

Fase 2 (1-2 meses)
- Integração com AWS KMS para gerenciamento de chaves
- Persistência em Postgres e armazenamento em S3
- Autenticação forte para API (OAuth2 / mTLS)
- Melhoria do modelo de anomalias (feature engineering, model drift)

Fase 3 (2-3 meses)
- Harden infra (HSM/KMS policies, VPC, secrets manager)
- CI/CD completo com SCA, SBOM e deploy automatizado
- Monitoramento e alerting (Prometheus/Grafana)
- Revisões de segurança e pentest
