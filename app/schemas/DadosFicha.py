from pydantic import BaseModel


class DadosFicha(BaseModel):
    """
    Essas três propriedades virão do front-end, onde o analista as inserirá.

    id: Id do chamado no Tomticket\n
    terminais: Quantidade de terminais para o cliente\n
    sc: Serviço de Cartão a ser configurado
    """

    id: str
    terminais: int
    sc: str
