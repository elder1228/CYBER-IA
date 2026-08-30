Objetivo
- Adicionar/ajustar o dashboard POC (frontend estático) e garantir integração com o backend para as operações principais.

O que contém este PR
- frontend/index.html, frontend/styles.css, frontend/script.js (dashboard POC)
- Pequenas validações de formulário no JS e mensagens de erro amigáveis

Arquivos principais a revisar
- frontend/index.html
- frontend/styles.css
- frontend/script.js

Como testar localmente
Opção A (recomendado): docker-compose up --build (backend serve assets estáticos em /)  
Opção B: cd frontend && python -m http.server 8080 — abra http://localhost:8080 e aponte o backend se necessário

Testar interações
- Gerar chave (/generate-key)  
- Upload/Encrypt de arquivo  
- Upload de logs (/upload-logs)  
- Chat (POST /chat)

Checklist de revisão
- [ ] Interações com o backend funcionam localmente  
- [ ] Inputs possuem validação mínima  
- [ ] Nenhum secret embutido em arquivos frontend  
- [ ] UX básico aceitável em desktop/mobile