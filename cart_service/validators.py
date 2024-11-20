from fastapi import HTTPException, status
from .models import CartItemsModel
from .schema import AddToCart
from pydantic import ValidationError


def validate_cart_items(item: AddToCart):
    try:
        CartItemsModel(username=item.username, items=[item for item in item.items])
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "http_error_code": "400",
                "error_msg": f"{e}",
            },
        )
    try:
        (int(item.product_id) for item in item.items)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "http_error_code": "400",
                "error": f"{e}",
                "example": "the product_id string should be integers e.g: '3455'",
            },
        )


def validate_offset_limit(offset: int, limit: int):
    if not isinstance(offset, int):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Invalid query parameter!"},
        )
    if not isinstance(limit, int):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Invalid query parameter!"},
        )


def validate_username(username: str):
    if not isinstance(username, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Invalid username!"},
        )
