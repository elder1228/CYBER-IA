# CYBER-IA

POC: Ferramenta de Cybersegurança + IA — criptografia, análise de logs (anomalies) e assistente IA.

Repositório contém:
- backend/ (FastAPI)
- frontend/ (dashboard estático)
- docker-compose.yml (api, postgres, minio)
- infra/terraform/ (templates AWS: KMS, RDS, S3, DynamoDB)
- .github/workflows/ (CI, publish GHCR, deploy Railway)

Quickstart local
1) Copie .env.example para .env e ajuste variáveis necessárias
2) docker-compose up --build
3) Acesse frontend: http://localhost:8080 (ou, se integrada, http://localhost:8000)

Executando backend local sem docker
- python -m venv .venv
- source .venv/bin/activate
- pip install -r backend/requirements.txt
- cd backend
- uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

CI/CD
- Actions: CI roda flake8, pytest, CodeQL. Publicação da imagem para GHCR ocorre quando CI passa.
- Deploy para Railway está disponível via workflow (configure RAILWAY_TOKEN e RAILWAY_PROJECT_ID nos Secrets)

Notas de segurança
- Não commit secrets ao repositório. Use GitHub Secrets para CI/CD.
- KMS/RDS/S3 geram custos na sua conta AWS.
