from src.app.schemas.emails_schemas import EmailBody, EmailScheduleBody, UUIDField
from marshmallow import ValidationError

class EmailsValidator():
    """ Validator for email-related operations """
    def __init__(self):
        self.email_body = EmailBody()
        self.email_schedule_body = EmailScheduleBody()
        self.uuid_field = UUIDField()
        
    """ Validate the format of an email address """
    def validate_email_body(self, email: dict) -> tuple[bool, dict | str]:
        try:
            validated_body = self.email_body.load(email)
            return True, validated_body
        except ValidationError as error:
            return False, error.messages

    """ Validate the subject of the email """
    def validate_content_type(self, content_type: str) -> bool:
        if not "text/plain" in content_type and not "text/html" in content_type:
            return False
        return True
    
    """ Validate the UUID """
    def validating_uuid(self, uuid: str) -> tuple[bool, str]:
        try:
            uuid_validated = self.uuid_field.load({"id": uuid})
            return True, uuid_validated["id"]
        except ValidationError as e:
            return False, str(e)
    
    """ Validate the schedule email body """
    def validate_schedule_email_body(self, body: dict) -> tuple[bool, dict | str]:
        try:
            validated_body = self.email_schedule_body.load(body)
            return True, validated_body
        except ValidationError as error:
            return False, error.messages