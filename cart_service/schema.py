from pydantic import BaseModel
from typing import List


class Cart_Items_IN(BaseModel):
    """This schema defines the fields of the cart items post data

    Args:
        BaseModel (class):
    """

    product_id: str
    quantity: int
    price: float


class Cart_Items_OUT(Cart_Items_IN):
    """Cart Items Model

    Args:
        Cart_Items_IN (user defined pydantic class):
    """

    total_price: float


class CartItems_ResponseModel(BaseModel):
    """Response Model

    Args:
        BaseModel (class):
    """

    data: Cart_Items_OUT | List[Cart_Items_OUT]
