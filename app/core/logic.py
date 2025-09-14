# app/core/logic.py
from app.schemas import DadosFicha
from app.core.get_data import get_ticket_data, get_conta_empresa_loja
from app.core.load_env import load_env


def gera_ficha(dados: DadosFicha):
    ID = dados.id
    TERMINAIS = dados.terminais
    SC = dados.sc

    # encapsular esse logica num try except e usar ifs p validar dpois
    CUSTOMER_URL, TICKET_URL, HEADER = load_env()

    ticket_data = get_ticket_data(TICKET_URL, ID, HEADER)

    conta_empresa_loja = get_conta_empresa_loja(ticket_data)

    resultado = {
        "status": "Dados do Tomticket obtidos com sucesso",
        "id_processado": ID,
        "conta_loja_encontrada": conta_empresa_loja,
        # "dados_completos_ticket": ticket_data,
    }
    print(resultado)
    return resultado
