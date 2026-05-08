# Projeto desenvolvido com auxílio da IA Gemini
from pydantic import BaseModel, Field
from enum import Enum
from typing import List

class TipoTransacao(str, Enum):
    deposito = "deposito"
    saque = "saque"

class TransacaoBase(BaseModel):
    valor: float = Field(gt=0, description="O valor deve ser positivo")
    tipo: TipoTransacao

class TransacaoCreate(TransacaoBase):
    pass

class Transacao(TransacaoBase):
    id: int
    
    class Config:
        from_attributes = True

class Extrato(BaseModel):
    saldo: float
    historico: List[Transacao]
