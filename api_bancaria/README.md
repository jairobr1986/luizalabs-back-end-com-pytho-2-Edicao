# 💰 API Bancária Assíncrona - Luizalabs

Este projeto é uma API RESTful assíncrona desenvolvida como parte de um desafio técnico. A aplicação gerencia operações bancárias básicas (depósitos e saques) utilizando práticas modernas de desenvolvimento backend com Python.

---

## 🤖 Desenvolvimento com IA
Este projeto foi desenvolvido com o suporte estratégico da **IA Gemini (Google)**. A colaboração incluiu:
- Arquitetura da estrutura de pastas.
- Implementação de lógica assíncrona com FastAPI.
- Configuração de esquemas de validação Pydantic.
- Estruturação de autenticação JWT segura.

---

## 🚀 Tecnologias Utilizadas
- **Python 3.14** (Ambiente de desenvolvimento)
- **FastAPI**: Framework web moderno e de alta performance.
- **Pydantic**: Validação de dados e tipos.
- **JWT (JSON Web Tokens)**: Segurança e autenticação.
- **Uvicorn**: Servidor ASGI de produção.

## 🛠️ Funcionalidades
- [x] **Cadastro de Transações**: Depósitos e saques com validação de saldo.
- [x] **Extrato**: Histórico de transações vinculado à conta.
- [x] **Segurança**: Endpoints protegidos por autenticação JWT.
- [x] **Documentação Automática**: Swagger UI disponível em `/docs`.

## 📦 Como rodar o projeto

1. **Crie o ambiente virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
