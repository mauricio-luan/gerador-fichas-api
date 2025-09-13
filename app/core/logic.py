from load_env import load_env
from get_data import get_ticket_data, get_customer_data


def main(id_ticket, qtd_terminais, servico_cartao):
    customer_url, ticket_url, header = load_env()

    ticket_data, conta_empresa_loja = get_ticket_data(ticket_url, id_ticket, header)

    customer_data = get_customer_data(customer_url, conta_empresa_loja, header)
