from fastapi import FastAPI
from app.routers import prediction
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug
)

app = FastAPI()



@app.get("/")
def home():
    return {"message": "FastAPI is working!"}

app.include_router(prediction.router)