def get_model():
    from app.models.model import model
    return model

from app.db.database import SessionLocal


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()