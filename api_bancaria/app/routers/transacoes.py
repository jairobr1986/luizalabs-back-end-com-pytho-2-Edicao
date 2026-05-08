# Projeto desenvolvido com auxílio da IA Gemini
from fastapi import APIRouter, HTTPException, Depends
from app import schemas, auth

router = APIRouter(prefix="/transacoes", tags=["Transações"])

# Mock de dados (Simulando banco de dados)
db_memoria = {
    "transacoes": [],
    "saldo": 0.0
}

@router.post("/", response_model=schemas.Transacao)
async def criar_transacao(transacao: schemas.TransacaoCreate):
    # Validação de saldo para saques
    if transacao.tipo == "saque":
        if db_memoria["saldo"] < transacao.valor:
            raise HTTPException(status_code=400, detail="Saldo insuficiente para esta operação.")
        db_memoria["saldo"] -= transacao.valor
    else:
        db_memoria["saldo"] += transacao.valor
        
    nova_transacao = {
        "id": len(db_memoria["transacoes"]) + 1,
        "valor": transacao.valor,
        "tipo": transacao.tipo
    }
    
    db_memoria["transacoes"].append(nova_transacao)
    return nova_transacao

# AGORA O EXTRATO EXIGE LOGIN (token)
@router.get("/extrato", response_model=schemas.Extrato)
async def visualizar_extrato(current_user: str = Depends(auth.get_current_user)):
    return {
        "saldo": db_memoria["saldo"],
        "historico": db_memoria["transacoes"]
    }