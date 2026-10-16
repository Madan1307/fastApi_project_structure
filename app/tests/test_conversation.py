from app.db.database import SessionLocal
from app.services.conversation_service import create_conversation


def test_create_conversation():
    db = SessionLocal()

    conversation = create_conversation(
        db,
        "Test Conversation"
    )

    assert conversation.id is not None
    assert conversation.title == "Test Conversation"

    db.close()
    