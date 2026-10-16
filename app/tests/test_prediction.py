from app.db.database import SessionLocal
from app.services.prediction_db_service import save_prediction


def test_save_prediction():
    db = SessionLocal()

    prediction = save_prediction(
        db=db,
        conversation_id=1,
        prediction=0
    )

    assert prediction.id is not None
    assert prediction.conversation_id == 1
    assert prediction.prediction == 0

    db.close()