from fastapi import HTTPException, status
from .models import Cart_Items
from .schema import Cart_Items_IN
from pydantic import ValidationError


def validate_cart_items(item: Cart_Items_IN):
    """validate the input of the cart items

    Args:
        item (Cart_Items_IN): pydantic class object.

    Raises:
        HTTPException: returns error message to the browser
        HTTPException: returns error message to the browser
    """
    try:
        Cart_Items(**item.model_dump())
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "http_error_code": "400",
                "error_msg": f"{e}",
            },
        )
    try:
        int(item.product_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "http_error_code": "400",
                "error": f"{e}",
                "example": "the product_id string should be integers e.g: '3455'",
            },
        )
