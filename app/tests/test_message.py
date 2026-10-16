from app.db.database import SessionLocal
from app.services.message_service import create_message


def test_create_message():
    db = SessionLocal()

    message = create_message(
        db,
        conversation_id=1,
        role="user",
        content="Test message"
    )

    assert message.id is not None
    assert message.conversation_id == 1
    assert message.role == "user"
    assert message.content == "Test message"

    db.close()