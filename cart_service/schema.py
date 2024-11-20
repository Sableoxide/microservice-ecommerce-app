from pydantic import BaseModel
from typing import List


class CartItems(BaseModel):
    product_id: str
    quantity: int
    price: float


class AddToCart(BaseModel):
    username: str
    items: List[CartItems]


class GetCart(BaseModel):
    _id: str | None = None
    username: str
    items: List[CartItems]
    total_price: float | None


class CartResponseModel(BaseModel):
    data: GetCart
