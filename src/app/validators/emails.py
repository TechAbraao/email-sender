from src.app.schemas.emails import EmailBody
from marshmallow import ValidationError

class EmailsValidator():
    """ Validator for email-related operations """
    def __init__(self):
        self.email_body = EmailBody()
    
    """ Validate the format of an email address """
    def validate_email_body(self, email: dict) -> tuple[bool, dict | str]:
        """
        Validate the format of the email body using the provided schema.
        return (True, validated_body) or (False, errors).
        """
        try:
            validated_body = self.email_body.load(email)
            return True, validated_body
        except ValidationError as error:
            return False, error.messages

    def validate_content_type(self, content_type: str) -> bool:
        """
        Validate the content type of the email body.
        Returns True if valid, False otherwise.
        """
        if not "text/plain" in content_type and not "text/html" in content_type:
            return False
        return True