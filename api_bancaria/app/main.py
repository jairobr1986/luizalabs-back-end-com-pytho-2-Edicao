# Projeto desenvolvido com auxílio da IA Gemini
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.routers import transacoes
from app import auth

app = FastAPI(title="API Bancária Luizalabs", description="Desafio de API Assíncrona")

# Rota para gerar o Token de acesso
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Usuário e senha "fake" para teste
    if form_data.username != "jairo" or form_data.password != "123456":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

app.include_router(transacoes.router)

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API Bancária Assíncrona!"}