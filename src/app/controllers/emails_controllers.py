from flask import jsonify
from src.app.validators.emails import EmailsValidator
from src.app.services.emails_services import EmailsService
from src.app.repository.emails_repository import EmailsRepository
from src.app.models.emails_model import EmailContentType

class EmailsController():
    """ This file contains the EmailsController class which handles email-related operations. """
    def __init__(self):
        self.service = EmailsService()
        self.validator = EmailsValidator()
        self.repository = EmailsRepository()
        
    def send_email(self, email_body: dict):
        validated_email_body, errors_or_email = self.validator.validate_email_body(email_body)
        if not validated_email_body:
            return jsonify({"success": False, "errors": errors_or_email}), 400
        
        validated_content_type = self.validator.validate_content_type(email_body.get("content_type", ""))
        if not validated_content_type:
            return jsonify({"success": False, "errors": "Invalid content type"}), 400
        
        sending_email = self.service.send_email(email_body)
        if not sending_email[0]:
            return jsonify({"success": False, "error": sending_email[1]["error"]}), 500
        
        """ Prepare the email body for saving in the database """
        email_body["content_type"] = EmailContentType(email_body["content_type"])
        saving_email_record = self.repository.create(email_body)
        if not saving_email_record[0]:
            return jsonify({"success": saving_email_record[0], "error": saving_email_record[1]}), 500
        
        return jsonify(sending_email[1]), 200

    def schedule_email(self, email_body: dict):
        """ This method is not implemented yet. """
        return jsonify({"message": "This feature is not implemented yet"}), 501