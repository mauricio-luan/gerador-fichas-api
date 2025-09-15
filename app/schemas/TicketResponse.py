"""
 Essas classes representam a estrutura da resposta
 a requisição do ticket, na api do Tomticket:
 {
    "data": {
        "protocol": 12345,
        "customer": {
            "internal_id": "008649-003798-0001",
        },
    }
}
"""

from pydantic import BaseModel


class Customer(BaseModel):
    internal_id: str


class Data(BaseModel):
    protocol: int
    customer: Customer


class TicketResponse(BaseModel):
    data: Data
    success: bool
