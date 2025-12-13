from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class GuestbookMessage(Base):
    __tablename__ = "guestbook_messages"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32))
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
