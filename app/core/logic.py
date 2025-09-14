# app/core/logic.py
import datetime
from app.core.get_data import get_ticket, get_customer
from app.core.load_env import load_env
from app.schemas.Ficha import InputUsuario, Ficha
from app.schemas.CustomerResponse import CustomerResponse
from app.schemas.TicketResponse import TicketResponse


def gera_ficha(input_usuario: InputUsuario) -> Ficha:
    CUSTOMER_URL, TICKET_URL, HEADER = load_env()

    ticket = TicketResponse.model_validate(
        get_ticket(TICKET_URL, input_usuario.id, HEADER)
    )

    customer = CustomerResponse.model_validate(
        get_customer(CUSTOMER_URL, ticket.data.customer.internal_id, HEADER)
    )

    return monta_ficha(
        ticket,
        customer,
        input_usuario.terminais,
        input_usuario.sc,
    )


def monta_ficha(
    ticket: TicketResponse,
    customer: CustomerResponse,
    terminais: int,
    servico_cartao: str,
) -> Ficha:
    chamado = ticket.data.protocol
    razao_social = customer.data[0].name

    # Captura das informações do customer
    custom_fields = customer.data[0].custom_fields
    mapa = {campo.name: campo.value for campo in custom_fields}

    internal_id = customer.data[0].internal_id
    conta, empresa, loja = internal_id.split("-")
    tokens = get_tokens(internal_id, terminais)

    # retornar aqui depois a funcao de criação da plnilha
    return Ficha(
        chamado=f"{chamado} - {datetime.datetime.now().strftime("%d/%m/%Y")}",
        nome_fantasia=mapa.get("Nome Fantasia").strip(),
        razao_social=razao_social.strip(),
        cnpj=mapa.get("CNPJ").strip(),
        endereco=f"{mapa.get('Endereco')}, {mapa.get('Numero')}".upper(),
        bairro=mapa.get("Bairro").upper().strip(),
        cidade=mapa.get("Cidade").upper().strip(),
        contato=mapa.get("COMERCIAL - Contato").upper().strip(),
        telefone=mapa.get("COMERCIAL - Telefone").strip(),
        email=mapa.get("COMERCIAL - E-mail").strip(),
        account=f"{conta} - {razao_social}".strip(),
        company=f"{empresa} - {razao_social}".strip(),
        store=f"{loja} - {mapa.get('Nome Fantasia')}".strip(),
        token=" / ".join(tokens),
        servico_cartao=servico_cartao.strip(),
    )


def get_tokens(internal_id: str, terminais: int) -> list[str]:
    partes = internal_id.split("-")
    tokens = []

    for i in range(1, int(terminais) + 1):
        tokens.append(f"{partes[1]}{partes[2]}{str(i).zfill(2)}")

    return tokens
