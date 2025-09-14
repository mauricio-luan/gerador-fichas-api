import requests


def get_ticket(url, id_ticket, header):
    try:
        response = requests.get(f"{url}{id_ticket}", headers=header)
        response.raise_for_status()
        ticket_data = response.json()

        return ticket_data
    except requests.exceptions.RequestException as e:
        return {"Erro": f"Erro ao obter os dados do ticket: {e}"}


def get_customer(url, internal_id, header):
    try:
        response = requests.get(f"{url}{internal_id}", headers=header)
        response.raise_for_status()
        customer_data = response.json()

        return customer_data
    except requests.exceptions.RequestException as e:
        return {"Erro": f"Erro ao obter os dados do customer: {e}"}
