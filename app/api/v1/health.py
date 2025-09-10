from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=str)
async def check_api_health():
    """Health check for API"""
    return "API is working"
