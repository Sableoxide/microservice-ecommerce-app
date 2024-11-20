from beanie import Document
from typing import List
from pydantic import Field
from .schema import CartItems


class CartItemsModel(Document):
    username: str
    items: List[CartItems]
    total_price: float | None = Field(default=None)

    async def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            price = item.price * item.quantity
            total_price += price
        self.total_price = total_price
        await self.save()

    class Settings:
        name = "cart_items"
        indexes = ["product_id"]
