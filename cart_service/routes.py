from fastapi import status
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from pymongo import errors

from .models import Cart_Items
from .schema import Cart_Items_IN, CartItems_ResponseModel
from .input_validators import validate_cart_items

cart_service = APIRouter(prefix="/cart", tags=["CART MICROSERVICE"])


@cart_service.post("")
async def add_to_cart(item: Cart_Items_IN):
    validate_cart_items(item)
    cart_item = Cart_Items(**item.model_dump())
    try:
        await cart_item.insert()
    except errors.DuplicateKeyError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error_message": "The product item already exists"},
        )
    await cart_item.calculate_total_price()
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": "Item added to cart",
            "item": {**item.model_dump()},
        },
    )


@cart_service.get("", response_model=CartItems_ResponseModel)
async def get_all_cart_items():
    """gets all cart items for the user on the db

    Returns:
        JSON
    """
    cart_items = await Cart_Items.all().to_list()
    return {"data": cart_items}
