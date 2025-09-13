import os
from dotenv import load_dotenv


def load_env():
    try:
        load_dotenv()
        CUSTOMER_URL = os.getenv("CUSTOMER_URL")
        TICKET_URL = os.getenv("TICKET_URL")
        API_TOKEN = os.getenv("API_TOKEN")
        HEADER = {"Authorization": f"Bearer {API_TOKEN}"}

        return CUSTOMER_URL, TICKET_URL, HEADER

    except Exception as e:
        # raise (f"Erro: {e}")
        return None, None, None
