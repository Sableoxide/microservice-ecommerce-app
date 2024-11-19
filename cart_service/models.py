from beanie import Document
from pydantic import Field
from pymongo import IndexModel

class Cart_Items(Document):
    product_id: str
    quantity: int
    price: float
    total_price: float | None = Field(default=None)
    
    async def calculate_total_price(self):
        self.total_price = self.price * self.quantity
        await self.save()
           

    class Settings:
        name = "cart_items"
        indexes = [
            IndexModel([("product_id", 1)], unique = True)
        ]
        