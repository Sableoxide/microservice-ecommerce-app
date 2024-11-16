from fastapi.routing import APIRouter
from pymongo import errors

from .models import Cart_Items
from .input_validators import validate_cart_items

cart_service = APIRouter(prefix="/cart", tags=["CART MICROSERVICE"])

@cart_service.post("/")
async def add_to_cart(item: dict):
    validate_cart_items(item)
    cart_item = Cart_Items(**item) 
    try:
        await cart_item.insert()
    except errors.DuplicateKeyError as e:
        return {"error_message": e}
    return {"message": "Item added to cart", "product_id": f"{cart_item.product_id}"}