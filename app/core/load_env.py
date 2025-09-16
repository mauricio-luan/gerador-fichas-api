import os
from dotenv import load_dotenv


def load_env():
    """
    Carrega as variáveis de ambiente do arquivo .env e retorna as URLs do Customer e do
    Ticket, além do header para o get na API do Tomticket.
    """
    load_dotenv()

    CUSTOMER_URL = os.getenv("CUSTOMER_URL")
    TICKET_URL = os.getenv("TICKET_URL")
    API_TOKEN = os.getenv("API_TOKEN")

    if not all([CUSTOMER_URL, TICKET_URL, API_TOKEN]):
        raise EnvironmentError("Nao foi possivel carregar as variaveis de ambiente.")

    HEADER = {"Authorization": f"Bearer {API_TOKEN}"}

    return CUSTOMER_URL, TICKET_URL, HEADER
