from fastapi import HTTPException, status
from .models import Cart_Items
from pydantic import ValidationError

def validate_cart_items(item: dict):
    try:
        Cart_Items(**item)  
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail = {
                "http_error_code": "400",
                "error_msg": f"{e}",
            }
        )
    try:
        int(item["product_id"])
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail = {
                "http_error_code": "400",
                "error": f"{e}",
                "example": "the string should be integers e.g: '3455'",
            }
        )