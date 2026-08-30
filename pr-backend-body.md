Objetivo
- Integrar o frontend estático ao backend FastAPI, adicionar/ajustar endpoints e incluir testes básicos de POC.

O que contém este PR
- Ajustes em backend/app/main.py para servir assets estáticos (integração do frontend).
- Testes adicionais em backend/tests/ (pytest).
- Pequenas melhorias no Dockerfile/start scripts para desenvolvimento local.
- Remoção de quaisquer referências a secrets hard-coded.

Arquivos principais a revisar
- backend/app/main.py
- backend/tests/*
- backend/Dockerfile
- docker-compose.yml

Como testar localmente
1) Copie .env.example → .env e preencha valores mínimos (POSTGRES_PASSWORD, MINIO_ACCESS_KEY/SECRET, SECRET_KEY).  
2) docker-compose up --build  
3) Verificar:
   - API: http://localhost:8000 → endpoints (/generate-key, /encrypt, /decrypt, /upload-logs, /analyze, /chat)  
   - Frontend integrado: http://localhost:8000  
4) Rodar testes:
   - pytest backend

Checklist de revisão
- [ ] Todos os testes passam (pytest)  
- [ ] Lint (flake8) rodou sem erros críticos  
- [ ] Nenhum secret em commits  
- [ ] Endpoints retornam códigos HTTP adequados e mensagens de erro claras  
- [ ] Documentação mínima (README) atualizada se necessário

Avisos de segurança / notas
- Em produção, substituir generate_key/fernet por envelope encryption com KMS. Não aplicar mudanças dependentes de KMS/RDS sem configurar secrets e permissões adequadas.