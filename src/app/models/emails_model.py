from sqlalchemy import Column, String, DateTime, UUID, Enum

class EmailStatus(Enum):
    """ Enum for email status """
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"

class EmailContentType(Enum):
    """ Enum for email content types """
    TEXT = "text/plain"
    HTML = "text/html"

class EmailsModel():
    """ Model for Emails """
    __tablename__ = 'emails'
    
    id = Column(UUID, primary_key=True)
    subject = Column(String(40), nullable=False) 
    to = Column(String(100), nullable=False)
    body = Column(String(300), nullable=False)
    content_type = Column(Enum(EmailContentType), nullable=False)
    scheduled_for = Column(DateTime, nullable=True)
    status = Column(Enum(EmailStatus), default=EmailStatus.SENT, nullable=False)
    created_at = Column(DateTime, nullable=False)