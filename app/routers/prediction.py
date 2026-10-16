from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.prediction_service import make_prediction
from app.services.prediction_db_service import save_prediction
from app.core.dependencies import get_model, get_db

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(
    data: PredictionRequest,
    model=Depends(get_model),
    db: Session = Depends(get_db)
):
    result = make_prediction(data, model)

    save_prediction(
        db,
        data.conversation_id,
        result
    )

    return {
        "prediction": result
    }