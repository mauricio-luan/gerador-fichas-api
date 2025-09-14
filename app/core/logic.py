# app/core/logic.py
from app.schemas.DadosFicha import DadosFicha
from app.schemas.Ficha import Ficha
from app.schemas.TicketResponse import TicketResponse
from app.schemas.CustomerResponse import CustomerResponse
from app.core.get_data import get_ticket_data, get_customer_data
from app.core.load_env import load_env


def gera_ficha(dados: DadosFicha):
    ID = dados.id
    # TERMINAIS = dados.terminais
    # SC = dados.sc

    CUSTOMER_URL, TICKET_URL, HEADER = load_env()

    ticket_data = get_ticket_data(TICKET_URL, ID, HEADER)
    ticket = TicketResponse.model_validate(ticket_data)
    conta_empresa_loja = ticket.data.customer.internal_id

    customer_data = get_customer_data(CUSTOMER_URL, conta_empresa_loja, HEADER)
    customer = CustomerResponse.model_validate(customer_data)

    ficha = monta_ficha(ticket, customer)

    return ficha


def monta_ficha(ticket: TicketResponse, customer: CustomerResponse) -> Ficha:
    protocol = ticket.data.protocol
    interal_id = ticket.data.customer.internal_id
    name = customer.data.name

    ficha = Ficha(chamado=protocol, account_company_store=interal_id, razao_social=name)

    return ficha
