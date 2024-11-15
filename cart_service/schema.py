from pydantic import BaseModel

class Cart_Items(BaseModel):
    product_ID: int
    quantity: int
    total_price: float
    
    