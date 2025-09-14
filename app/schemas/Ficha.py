from pydantic import BaseModel
from typing import Optional


class InputUsuario(BaseModel):
    """
    Essas três propriedades virão do front-end, onde o analista as inserirá.

    id: Id do chamado no Tomticket\n
    terminais: Quantidade de terminais para o cliente\n
    sc: Serviço de Cartão a ser configurado
    """

    id: str
    terminais: int
    sc: str


class Ficha(BaseModel):
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
