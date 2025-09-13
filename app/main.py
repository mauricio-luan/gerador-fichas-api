# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Gerador de Fichas Online",
    description="...",
    version="0.1.0",
)


class informacoesFicha(BaseModel):
    id_ticket: str
    qtd_terminais: int
    servico_cartao: str


class ModeloDeSaida(BaseModel):
    id: int
    dados_processados: str


@app.get("/")
def ler_raiz():
    """
    Endpoint principal da API. Retorna uma mensagem de boas-vindas.
    """
    return {"mensagem": "Bem-vindo à minha API!"}


@app.post("/recursos/", response_model=ModeloDeSaida)
def criar_recurso(dados_entrada: informacoesFicha):
    """
    Recebe dados, processa-os e cria um novo recurso no sistema.
    """

    resultado_processamento = f"Processado: {dados_entrada.campo_obrigatorio.upper()}"

    return ModeloDeSaida(dados_processados=resultado_processamento)


# Adicione aqui outros endpoints conforme sua necessidade:
# @app.get("/recursos/{recurso_id}") ...
# @app.put("/recursos/{recurso_id}") ...
# @app.delete("/recursos/{recurso_id}") ...
