def get_chamado(ticket_data):
    try:
        if not ticket_data:
            raise Exception(f"Param: {ticket_data} está vazio")

        chamado = ticket_data["data"]["protocol"]

        return chamado
    except Exception as e:
        return {"Erro": f"Erro ao obter os dados do ticket: {e}"}
