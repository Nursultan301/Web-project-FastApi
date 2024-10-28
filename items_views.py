from typing import Annotated

from fastapi import Path, APIRouter

router = APIRouter(prefix="/items", tags=["items"])



@router.get("/")
def items():
    return [
        "item1",
        "item2",
    ]

@router.get("/latest/")
def get_latest():
    return {"items": {"id": 0, "name": "LATEST"}}


@router.get("/{item_id}/")
def  get_item(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {"item": {
            "id": item_id,
        }}
