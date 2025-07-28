from sqlalchemy import Column, String, DateTime, UUID, Enum as SQLAlchemyEnum
from src.app.database.configs_database import Base
from enum import Enum as PyEnum


class EmailStatus(PyEnum):
    """ Enum for email status """
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"

class EmailContentType(PyEnum):
    """ Enum for email content types """
    TEXT = "text/plain"
    HTML = "text/html"

class EmailsModel(Base):
    """ Model for Emails """
    __tablename__ = 'emails'
    
    id = Column(UUID, primary_key=True)
    subject = Column(String(40), nullable=False) 
    to = Column(String(100), nullable=False)
    body = Column(String(2000), nullable=False)
    content_type = Column(SQLAlchemyEnum(EmailContentType), nullable=False)
    scheduled_for = Column(DateTime, nullable=True)
    status = Column(SQLAlchemyEnum(EmailStatus), default=EmailStatus.SENT, nullable=False)
    created_at = Column(DateTime, nullable=False)