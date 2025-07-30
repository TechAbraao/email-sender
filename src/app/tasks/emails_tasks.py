from src.app.celery_app import celery_app
from src.app.services.emails_services import EmailsService

@celery_app.task
def send_email_task(email_body: dict) -> tuple[bool, dict[str, str]]:
    service = EmailsService()
    return service.send_email(email_body)
