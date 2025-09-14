import os
from dotenv import load_dotenv


def load_env():
    """
    Carrega as variáveis de ambiente do arquivo .env e retorna as URLs do Customer e do
    Ticket, além do header para o get na API do Tomticket.
    """
    try:
        dados_env = load_dotenv()
        if not dados_env:
            raise EnvironmentError(
                "Não foi possível carregar as variáveis de ambiente."
            )

        CUSTOMER_URL = os.getenv("CUSTOMER_URL")
        TICKET_URL = os.getenv("TICKET_URL")
        API_TOKEN = os.getenv("API_TOKEN")

        HEADER = {"Authorization": f"Bearer {API_TOKEN}"}

        return CUSTOMER_URL, TICKET_URL, HEADER
    except EnvironmentError as e:
        print(f"Erro: {e}")
        return None, None, None
