from fastapi.routing import APIRouter
from .models import Cart_Items


cart_service = APIRouter()

@cart_service.post("/cart/add")
async def add_to_cart(item: dict):
    cart_item = Cart_Items(**item)
    await cart_item.insert()
    return {"message": "Item added to cart", "product_id": f"{cart_item.product_id}"}