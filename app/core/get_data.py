import requests
from app.core.exceptions import (
    TomticketApiError,
    TicketNotFountError,
    AuthenticationError,
)


def get_ticket(url, id_ticket, header):
    try:
        response = requests.get(f"{url}{id_ticket}", headers=header)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            raise TicketNotFountError(f"Ticket '{id_ticket}' inválido.")
        elif e.response.status_code == 401:
            raise AuthenticationError("Token de autenticacao invalido.")
        else:
            raise TomticketApiError(f"Erro inesperado: {e.response.status_code}")


def get_customer(url, internal_id, header):
    try:
        response = requests.get(f"{url}{internal_id}", headers=header)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            raise TicketNotFountError(f"Customer '{internal_id}' nao encontrado.")
        else:
            raise TomticketApiError(f"Erro inesperado: {e.response.status_code}")
