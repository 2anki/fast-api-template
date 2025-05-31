from typing import Optional

from fastapi import APIRouter

from app.models.items import Item
from app.services.item_service import calculate_total_price

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Item not found"}},
)


@router.get("/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@router.post("/")
def create_item(item: Item):
    total = calculate_total_price(item)
    return {"name": item.name, "total_price": total}
