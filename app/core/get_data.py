import requests
from app.core.exceptions import TomticketApiError


def get_ticket(url, id_ticket, header):
    try:
        response = requests.get(f"{url}{id_ticket}", headers=header)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            raise TomticketApiError(f"Ticket {id_ticket} nao encontrado.")
        else:
            raise TomticketApiError(f"Erro ao obter os dados do ticket: {id_ticket}")


def get_customer(url, internal_id, header):
    try:
        response = requests.get(f"{url}{internal_id}", headers=header)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        raise TomticketApiError(f"Erro ao obter os dados do cliente {internal_id}.")
