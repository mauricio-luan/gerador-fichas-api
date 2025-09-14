from fastapi import FastAPI
from app.schemas.DadosFicha import DadosFicha
from app.core.logic import gera_ficha

app = FastAPI(
    title="Gerador de Fichas Online",
    description="Oferece a funcionalidade de criação de Ficha de Implantação via web.",
    version="0.1.0",
)


@app.get("/")
def raiz():
    mensagem = app.description
    return {"mensagem": mensagem}


@app.post("/fichas/")
def cria_ficha(input: DadosFicha):
    response = gera_ficha(input)
    return response
