# Integração Bling API + Firebird

Projeto demonstrativo independente para portfólio, reconstruído a partir da descrição funcional do projeto original. Não contém código, credenciais, banco de dados ou informações da antiga empresa.

## Objetivo
Demonstrar uma arquitetura básica em Python para:
- Consumir endpoints REST do Bling usando token informado por variável de ambiente.
- Tratar respostas JSON e erros HTTP.
- Persistir registros em uma base Firebird local, com uma camada simples de repositório.

## Status
**Base demonstrativa inicial.** Não representa a aplicação corporativa original nem inclui sincronização completa de pedidos, produtos, notas fiscais ou relatórios. Essas funcionalidades podem ser implementadas e testadas em etapas.

## Requisitos
- Python 3.10+
- Firebird Server acessível
- Credenciais e token próprios de uma conta de teste do Bling

## Instalação
```bash
python -m venv .venv
```

Windows:
```cmd
.venv\Scripts\activate
pip install -r requirements.txt
```

## Configuração
Defina as variáveis de ambiente no seu ambiente local. Nunca publique tokens, senhas ou arquivos de banco de dados.

Windows CMD:
```cmd
set BLING_ACCESS_TOKEN=seu_token_de_teste
set FIREBIRD_DATABASE=C:\\dados\\teste.fdb
set FIREBIRD_USER=SYSDBA
set FIREBIRD_PASSWORD=sua_senha_local
```

## Estrutura
- `src/bling_client.py`: cliente HTTP mínimo para chamadas autenticadas à API.
- `src/firebird_repository.py`: conexão e inserção parametrizada de exemplo no Firebird.
- `requirements.txt`: dependências.

## Segurança
- Não commitar arquivos `.env`, tokens, senhas, dumps ou bases de dados.
- Use apenas uma conta de teste e dados fictícios.
- Consulte a documentação oficial do Bling para os endpoints e limites atuais.

## Próximas etapas
1. Implementar OAuth 2.0 com fluxo adequado à aplicação.
2. Mapear endpoints e paginação da API.
3. Criar schema versionado e operações idempotentes.
4. Implementar sincronização incremental e testes automatizados.
5. Criar relatórios locais com dados sintéticos.
