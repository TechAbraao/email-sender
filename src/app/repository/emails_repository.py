from src.app.database.configs_database import SessionLocal
from src.app.models.emails_model import EmailsModel, EmailContentType, EmailStatus
from uuid import uuid4
from datetime import datetime
from zoneinfo import ZoneInfo

class EmailsRepository:
    def __init__(self):
        self.session = SessionLocal()
        self.validator = None
        
    def create(self, email) -> tuple[bool, str]:
        """ Create a new email record in the database. """
        try:            
            creating_email = EmailsModel(
                id=uuid4(),
                subject=email.get("subject"),
                to=email.get("to"),
                body=email.get("body"),
                content_type=EmailContentType(email.get("content_type")),
                scheduled_for=email.get("schedule_time", datetime.now(ZoneInfo("America/Sao_Paulo"))),
                status=email.get("status", EmailStatus.FAILED),
                created_at=datetime.now(ZoneInfo("America/Sao_Paulo")),
            )
            self.session.add(creating_email)
            self.session.commit()
            self.session.refresh(creating_email)
            
            return True, email
        except Exception as e:
            self.session.rollback()
            return False, str(e)    
        finally:
            self.session.close()
        
    def get_by_id(): pass
    
    def get_all(): pass
    
    def update(): pass
    
    def delete(): pass
