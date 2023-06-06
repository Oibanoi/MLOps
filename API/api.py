from fastapi import APIRouter

from API import api_predict

router = APIRouter()
router.include_router(api_predict.router, tags=["Predict"], prefix="")
