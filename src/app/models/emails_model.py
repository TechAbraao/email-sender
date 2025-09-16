from sqlalchemy import Column, String, DateTime, UUID, Enum as SQLAlchemyEnum
from src.app.utils.extesions import db
from enum import Enum as PyEnum


class EmailStatus(PyEnum):
    """ Enum for email status """
    PENDING = "pending"
    SENT = "sent"
    CANCELED = "canceled"
    FAILED = "failed"

class EmailContentType(PyEnum):
    """ Enum for email content types """
    TEXT = "text/plain"
    HTML = "text/html"

class EmailsModel(db.Model):
    """ Model for Emails """
    __tablename__ = 'emails'
    
    id = db.Column(UUID, primary_key=True)
    subject = db.Column(String(40), nullable=False)
    to = db.Column(String(100), nullable=False)
    body = db.Column(String(2000), nullable=False)
    content_type = db.Column(SQLAlchemyEnum(EmailContentType), nullable=False)
    scheduled_for = db.Column(DateTime, nullable=True)
    status = db.Column(SQLAlchemyEnum(EmailStatus, name="emailstatus"), default=EmailStatus.SENT, nullable=False)
    task_id = db.Column(UUID, nullable=True, unique=True)
    created_at = db.Column(DateTime, nullable=False)
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "subject": self.subject,
            "to": self.to,
            "body": self.body,
            "content_type": self.content_type.value,
            "scheduled_for": self.scheduled_for.isoformat() if self.scheduled_for else None,
            "status": self.status.value,
            "task_id": str(self.task_id) if self.task_id else None,
            "created_at": self.created_at.isoformat()
        }