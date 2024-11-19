from pydantic import BaseModel
from typing import List

class Cart_Items_IN(BaseModel):
    product_id: str
    quantity: int
    price: float
    
class Cart_Items_OUT(Cart_Items_IN):
    total_price: float
    
class CartItems_ResponseModel(BaseModel):
    data: Cart_Items_OUT | List[Cart_Items_OUT]