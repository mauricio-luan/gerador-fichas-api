"""Ponto de entrada principal da API Gerador de Fichas.

Este módulo utiliza o framework FastAPI para criar e expor os endpoints da aplicação.
Sua principal responsabilidade é atuar como a camada web (Web Layer), recebendo
as requisições HTTP, validando os dados de entrada através dos schemas Pydantic
e orquestrando as chamadas para a camada de lógica de negócio (`core/logic.py`).

Após a lógica de negócio ser executada, este módulo também é responsável por
converter o resultado final (a ficha) em uma resposta HTTP apropriada, como um
download de arquivo .xlsx.

Endpoints:
- GET /: Endpoint de boas-vindas para verificar o status da API.
- POST /fichas/: Recebe o ID do ticket e outros dados, executa todo o fluxo de
  busca de informações e retorna a ficha de implantação para download.
"""

__author__ = "Mauricio Luan"
__version__ = "0.1.0"
__email__ = "mauricioluan2023@exemplo.com"
__status__ = "Development"

import io
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from app.schemas.Ficha import InputUsuario
from app.core.gera_xlsx import gera_planilha
from app.core.logic import gera_ficha
from app.core.exceptions import (
    TomticketApiError,
    TicketNotFountError,
    AuthenticationError,
)

app = FastAPI(
    title="API Gerador de Fichas",
    description="Oferece a funcionalidade de criação de Ficha de Implantação via web.",
    version=__version__,
)


@app.get("/")
def raiz():
    mensagem = app.description
    return {"mensagem": mensagem}


@app.post("/fichas/")
def cria_ficha(input_usuario: InputUsuario):
    try:
        ficha = gera_ficha(input_usuario)
        workbook = gera_planilha(ficha)
        nome_arquivo = f"{ficha.store}.xlsx"

        buffer = io.BytesIO()
        workbook.save(buffer)
        buffer.seek(0)

        return StreamingResponse(
            buffer,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename={nome_arquivo}"},
        )
    except TicketNotFountError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except AuthenticationError as e:
        raise HTTPException(status_code=401, detail=str(e))

    except TomticketApiError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        print(f"ERRO INTERNO DO SERVIDOR: {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor.")
