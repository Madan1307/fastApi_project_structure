from pydantic import BaseModel

class PredictionRequest(BaseModel):
    conversation_id: int
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionResponse(BaseModel):
    prediction: int
    