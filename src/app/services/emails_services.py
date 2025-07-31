from src.app.settings.email_settings import EmailSettings
from email.mime.text import MIMEText
import smtplib
from celery.result import AsyncResult
from src.app.celery_app import celery_app
from src.app.repository.emails_repository import EmailsRepository
import logging

logger = logging.getLogger(__name__)

""" Service class for handling e-mail operations. """
class EmailsService:
    def __init__(self): 
        self.email_settings = EmailSettings()
        self.repository = EmailsRepository()
        self.celery_app = celery_app

    def send_email(self, email_body: dict) -> tuple[bool, dict[str, str]]:
        """ Sends an email using the provided email body. """
        subject = email_body.get('subject', '')
        to = email_body.get('to', '')
        body = email_body.get('body', '')
        content_type = email_body.get('content_type')

        msg = self.__mime_type(body, content_type)
        msg['Subject'] = subject
        msg['From'] = self.email_settings.smtp_email
        msg['To'] = to

        try:
            with smtplib.SMTP(self.email_settings.smtp_server, self.email_settings.smtp_port) as server:
                server.starttls()
                server.login(self.email_settings.smtp_email, self.email_settings.smtp_password)
                server.send_message(msg)

            return True, {"message": "E-mail sent successfully"}

        except Exception as err:
            return False, {"error": str(err)}

    def cancel_email_scheduling(self, task_id: str):
        """ """
        try:
            success, msg = self.repository.update_status_by_task_id(task_id, "canceled")
            if not success:
                return False, "Error updating scheduled email status", str(msg)
            AsyncResult(task_id, app=self.celery_app).revoke()
            return True, "Email schedule canceled successfully."
        except Exception as e:
            return False, str(e)

    def __mime_type(self, body: str, content_type: str) -> MIMEText:
        """ Returns a MIMEText object based on the content type. """
        if content_type == "text/plain":
            return MIMEText(body, 'plain')
        elif content_type == "text/html":
            return MIMEText(body, 'html')
        else:
            raise ValueError("Unsupported content type")
