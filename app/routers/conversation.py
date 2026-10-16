from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services.conversation_service import (
    create_conversation,
    get_conversations,
    get_conversation
)

router = APIRouter()


@router.post("/conversations")
def create(title: str, db: Session = Depends(get_db)):
    return create_conversation(db, title)


@router.get("/conversations")
def read_conversations(db: Session = Depends(get_db)):
    return get_conversations(db)


@router.get("/conversations/{conversation_id}")
def read_conversation(
    conversation_id: int,
    db: Session = Depends(get_db)
):
    return get_conversation(db, conversation_id)