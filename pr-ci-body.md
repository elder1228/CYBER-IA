Objetivo
- Adicionar workflows: CI (lint, pytest, build validation), CodeQL scan e publicação de imagem no GHCR. Incluir workflow opcional para deploy Railway (ativa se secrets configurados).

O que contém este PR
- .github/workflows/ci.yml (lint, pytest, build validation, CodeQL)  
- .github/workflows/publish-ghcr.yml (publicação GHCR)  
- .github/workflows/deploy-railway.yml (opcional)

Como testar
- Push para a branch dispara os workflows.  
- Verificar runs em Actions → CI (flake8, pytest), CodeQL, Publish (quando aplicável).

Checklist de revisão
- [ ] CI roda flake8 e pytest com sucesso  
- [ ] CodeQL configurado  
- [ ] Docker build validado (build-push-action com push: false em CI)  
- [ ] Publish to GHCR configurado (confirmar permissões do token/GITHUB_TOKEN)  
- [ ] Secrets necessários documentados no README

Avisos
- Configure corretamente os Secrets antes de permitir publicação GHCR / deploy Railway.