from fastapi import status, HTTPException
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from pymongo import errors

from .models import CartItemsModel
from .schema import AddToCart, CartResponseModel, GetCart
from .validators import validate_cart_items
from .validators import validate_offset_limit

cart_service = APIRouter(prefix="/cart", tags=["CART MICROSERVICE"])


# USER
@cart_service.post("")
async def add_to_cart(item: AddToCart):
    validate_cart_items(item)
    cart_item = CartItemsModel(
        username=item.username, items=[item for item in item.items]
    )
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


# ADMIN
@cart_service.get("{limit}/{offset}", response_model=CartResponseModel)
async def filter_cart_items(offset: int = 0, limit: int = 10):
    validate_offset_limit(offset=offset, limit=limit)
    cart_items = await CartItemsModel.find_many(skip=offset, limit=limit).to_list()
    return {"data": cart_items}


# USER
@cart_service.get("{username}", response_model=GetCart)
async def filter_cart_item(username: str | None = None):
    if username is not None:
        cart = await CartItemsModel.find_one(username=username)
        existing_username = cart.username
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Username is NULL!"},
        )
    if existing_username:
        if cart.items:
            return cart
        else:
            HTTPException(
                status_code=status.HTTP_204_NO_CONTENT,
                detail={"error": "The cart is EMPTY!!"},
            )
    else:
        HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "The user does not EXIST!!"},
        )
