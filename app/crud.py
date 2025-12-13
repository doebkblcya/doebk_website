from sqlalchemy.orm import Session
from app.models import GuestbookMessage
from datetime import datetime

def create_message(db: Session, name: str, message: str):
    db_message = GuestbookMessage(name=name, message=message, created_at=datetime.utcnow())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages(db: Session, skip: int = 0, limit: int = 20):
    return db.query(GuestbookMessage).order_by(GuestbookMessage.created_at.desc()).offset(skip).limit(limit).all()
