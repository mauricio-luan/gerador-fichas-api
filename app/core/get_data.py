import requests


def get_ticket_data(url, id_ticket, header):
    try:
        response = requests.get(f"{url}{id_ticket}", headers=header)
        response.raise_for_status()
        ticket_data = response.json()
        conta_empresa_loja = ticket_data["data"]["customer"]["internal_id_ticket"]

        return ticket_data, conta_empresa_loja
    except requests.exceptions.RequestException as e:
        # print(f"Erro ao obter dados do chamado: {e}")
        return None, None


def get_customer_data(url, conta_empresa_loja, header):
    try:
        response = requests.get(f"{url}{conta_empresa_loja}", headers=header)
        response.raise_for_status()
        customer_data = response.json()

        return customer_data
    except requests.exceptions.RequestException as e:
        # print(f"Erro ao obter dados do cliente: {e}")
        return None
