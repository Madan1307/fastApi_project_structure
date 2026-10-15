from fastapi import APIRouter,Depends
from app.schemas.prediction import PredictionRequest,PredictionResponse
from app.services.prediction_service import make_prediction
from app.core.dependencies import get_model
router = APIRouter()

@router.post("/predict",response_model=PredictionResponse)
def predict(data : PredictionRequest,model=Depends(get_model)):
    result = make_prediction(data,model)
    return {
        "prediction":result
    }



