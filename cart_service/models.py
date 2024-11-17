from beanie import Document

class Cart_Items(Document):
    product_id: str
    quantity: int
    total_price: float

    class Settings:
        name = "cart_items"
        indexes = ["product_id"] 