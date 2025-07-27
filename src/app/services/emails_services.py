from src.app.settings.email_settings import EmailSettings
from email.mime.text import MIMEText
import smtplib

""" Service class for handling e-mail operations. """
class EmailsService:
    def __init__(self): 
        self.email_settings = EmailSettings()
        self.server_smtp = smtplib.SMTP(self.email_settings.smtp_server, self.email_settings.smtp_port)
        
    def send_email(self, email_body: dict) -> tuple[bool, dict[str, str]]:
        """ Sends an email using the provided email body. """
        subject = email_body.get('subject', '')
        to = email_body.get('to', '')
        body = email_body.get('body', '')
        content_type = email_body.get('content_type')
        
        msg = self.__mime_type(body, content_type)
        
        try:
            msg['Subject'] = subject
            msg['From'] = self.email_settings.smtp_email
            msg['To'] = to
            
            # Connect to the SMTP server and send the email
            self.server_smtp.starttls()
            self.server_smtp.login(self.email_settings.smtp_email, self.email_settings.smtp_password)
            self.server_smtp.send_message(msg)
            self.server_smtp.quit()
            
            return True, {"message": "E-mail sent successfully"}
        except Exception as err:
            return False, {"error": str(err)}
        
    def __mime_type(self, body: str, content_type: str) -> MIMEText:
        """ Returns a MIMEText object based on the content type. """
        if content_type == "text/plain":
            return MIMEText(body, 'plain')
        elif content_type == "text/html":
            return MIMEText(body, 'html')
        else:
            raise ValueError("Unsupported content type")
        