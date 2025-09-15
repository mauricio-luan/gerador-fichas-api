from pydantic import BaseModel
from typing import Optional


class InputUsuario(BaseModel):
    """
    Representa as três propriedades que serão passadas pelo usuário lá no front.

    id: Id do chamado no Tomticket\n
    terminais: Quantidade de terminais para o cliente\n
    servico_cartao: Qual o serviço de cartão a ser configurado para o cliente
    """

    id: str
    terminais: int
    servico_cartao: str


class Ficha(BaseModel):
    """Representa a ficha de implantação."""

    chamado: str
    nome_fantasia: str
    razao_social: str
    cnpj: str
    endereco: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    contato: str
    telefone: Optional[str] = None
    email: str
    account: str
    company: str
    store: str
    token: str
    servico_cartao: Optional[str] = None
