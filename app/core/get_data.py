import requests


def get_ticket_data(url, id_ticket, header):
    try:
        response = requests.get(f"{url}{id_ticket}", headers=header)
        response.raise_for_status()
        ticket_data = response.json()

        return ticket_data
    except requests.exceptions.RequestException as e:
        return {"Erro": f"Erro ao obter os dados do ticket: {e}"}


def get_customer_data(url, conta_empresa_loja, header):
    try:
        response = requests.get(f"{url}{conta_empresa_loja}", headers=header)
        response.raise_for_status()
        customer_data = response.json()

        return customer_data
    except requests.exceptions.RequestException as e:
        return {"Erro": f"Erro ao obter os dados do customer: {e}"}
