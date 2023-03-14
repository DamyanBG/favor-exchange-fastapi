from fastapi import APIRouter

router = APIRouter(tags=["Works"])

@router.get(
    "/works/",
)
async def get_users():
    return "works"
