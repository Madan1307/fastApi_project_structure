from sqlalchemy.orm import Session
from app.models.prediction import Prediction


def save_prediction(
    db: Session,
    conversation_id: int,
    prediction: int
):
    saved_prediction = Prediction(
        conversation_id=conversation_id,
        prediction=prediction
    )

    db.add(saved_prediction)
    db.commit()
    db.refresh(saved_prediction)

    return saved_prediction