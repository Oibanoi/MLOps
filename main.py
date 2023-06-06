import uvicorn as uvicorn
from fastapi import FastAPI

from API.api import router


def get_application() -> FastAPI:
    application = FastAPI(
    )
    application.include_router(router)

    return application


app = get_application()
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
