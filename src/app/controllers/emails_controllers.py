from flask import jsonify
from src.app.validators.emails import EmailsValidator
from src.app.services.emails_services import EmailsService
from src.app.repository.emails_repository import EmailsRepository
from src.app.models.emails_model import EmailContentType
from src.app.tasks.emails_tasks import send_email_task, update_database_status_success_task, update_database_status_failure_task
from datetime import datetime
from zoneinfo import ZoneInfo

class EmailsController():
    """ This file contains the EmailsController class which handles email-related operations. """
    def __init__(self):
        self.service = EmailsService()
        self.validator = EmailsValidator()
        self.repository = EmailsRepository()
       
    """ Send an e-mail """
    def send_email(self, email_body: dict):
        validated_email_body, errors_or_email = self.validator.validate_email_body(email_body)
        if not validated_email_body:
            return jsonify({"success": False, "errors": errors_or_email}), 400
        
        validated_content_type = self.validator.validate_content_type(email_body.get("content_type", ""))
        if not validated_content_type:
            return jsonify({"success": False, "errors": "Invalid content type"}), 400
        
        """ Using .delay() to send the email asynchronously """
        sending_email = send_email_task.delay(
            email_body
            )
        
        """ Prepare the email body for saving in the database """
        email_body["content_type"] = EmailContentType(email_body["content_type"])
        email_body["status"] = "SENT"
        email_body["task_id"] = sending_email.id
        
        saving_email_record = self.repository.create(email_body)
        if not saving_email_record[0]:
            return jsonify({"success": saving_email_record[0], "error": saving_email_record[1]}), 500
        
        return jsonify({
            "message": "E-mail sent successfully.",
            "task_id": sending_email.id,
            }), 200
    
    """ Schedule an e-mail (not implemented yet) """
    def send_scheduled_email(self, email_body: dict):
        validated_email_body, errors_or_email = self.validator.validate_schedule_email_body(email_body)
        if not validated_email_body:
            return jsonify({"success": False, "errors": errors_or_email}), 400
        
        validated_content_type = self.validator.validate_content_type(email_body.get("content_type", ""))
        if not validated_content_type:
            return jsonify({"success": False, "errors": "Invalid content type"}), 400
        
        """ Asynchronously schedule the e-mail using a Celery task """
        schedule_time = email_body.get("schedule_time") 
        schedule_time_converted = datetime.fromisoformat(schedule_time).replace(tzinfo=ZoneInfo("America/Sao_Paulo"))

        time_now = datetime.now(ZoneInfo("America/Sao_Paulo"))
        delta = schedule_time_converted - time_now

        if delta.total_seconds() <= 0:
            return jsonify({"success": False, "error": "Scheduled time must be in the future"}), 400

        """ Using .apply_async() to schedule the task """
        sending_email = send_email_task.apply_async(
            args=[email_body], 
            eta=time_now + delta,
            link=update_database_status_success_task.s(),
            link_error=update_database_status_failure_task.s()
            )
        
        """ Prepare the email body for saving in the database """
        email_body["content_type"] = EmailContentType(email_body["content_type"])
        email_body["status"] = "PENDING"
        email_body["task_id"] = sending_email.id
        
        saving_email_record = self.repository.create(email_body)
        if not saving_email_record[0]:
            return jsonify({"success": saving_email_record[0], "error": saving_email_record[1]}), 500
        
        return jsonify({"message": "E-mail sent successfully."}), 200

    """ Get all scheduled and sent emails """
    def get_all_emails(self, status): 
        if not status:
            all_emails = self.repository.get_all(status=None)
            
            if isinstance(all_emails, tuple) and all_emails[0] is False:
                return jsonify({"success": False, "error": all_emails[1]}), 500
            
            if not all_emails:
                return jsonify({"success": False, "error": "No emails found"}), 404
            
            return jsonify({"success": True, "emails": [email.to_dict() for email in all_emails]}), 200
        else:
            all_emails_with_status = self.repository.get_all(status=status)
            
            if isinstance(all_emails_with_status, tuple) and all_emails_with_status[0] is False:
               return jsonify({"success": False, "error": all_emails_with_status[1]}), 500
            
            if not all_emails_with_status:
                return jsonify({"success": False, "error": "No emails found"}), 404
            
            return jsonify({"success": True, "emails": [email.to_dict() for email in all_emails_with_status]}), 200
        
    """ """
    def get_email_by_uuid(self, uuid: str):
        uuid_bool, uuid_value = self.validator.validating_uuid(uuid)
        if not uuid_bool:
            return jsonify({"success": False, "error": "This field is not UUID."}), 500
        
        email = self.repository.get_by_id(uuid_value)
        if not email:
            return jsonify({"success": False, "error": "Unable to find email."}), 204
        
        return jsonify({"success": True, "message": email[1]})