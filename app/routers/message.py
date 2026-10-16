from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services.message_service import create_message

router = APIRouter()


@router.post("/messages")
def create_new_message(
    conversation_id: int,
    role: str,
    content: str,
    db: Session = Depends(get_db)
):
    message = create_message(
        db,
        conversation_id,
        role,
        content
    )

    return message