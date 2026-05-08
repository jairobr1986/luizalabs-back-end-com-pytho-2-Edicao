# 💰 API Bancária Assíncrona - Desafio Luizalabs

Este projeto é uma API RESTful para gerenciamento de transações bancárias, desenvolvida com o framework FastAPI.

## 🤝 Desenvolvimento com IA
Este projeto foi construído com o suporte técnico da **IA Gemini (Google)**, que auxiliou na estruturação da arquitetura assíncrona, lógica de validação de saldo e implementação da camada de segurança JWT.

## 🚀 Funcionalidades
- **Depósitos e Saques**: Registro de operações com validação de valores positivos.
- **Validação de Saldo**: Impede saques superiores ao saldo disponível.
- **Extrato Protegido**: Visualização do histórico permitida apenas para usuários autenticados.
- **Segurança JWT**: Implementação de tokens OAuth2 para proteção de endpoints sensíveis.

## 🛠️ Tecnologias
- Python 3.14
- FastAPI
- Pydantic (Validação de Schemas)
- Jose (JWT)
- Passlib (Criptografia)

## 📖 Como Usar
1. Instale as dependências: `pip install -r requirements.txt`
2. Rode a aplicação: `python -m uvicorn app.main:app --reload`
3. Acesse `/docs` para testar.
   - **Login de Teste**: jairo / 123456