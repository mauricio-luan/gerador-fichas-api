from pydantic import BaseModel


class Ficha(BaseModel):
    chamado: int
    account_company_store: str
    razao_social: str


"""     nome_fantasia: str
    razao_social: str
    cnpj: str
    endereco: str
    bairro: str
    cidade: str
    contato: str
    telefone: str
    email: str
    conta: str
    empresa: str
    loja: str
    token: str
    servico_cartao: str """
