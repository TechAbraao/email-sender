from flask import Blueprint, request
from src.app.controllers.emails_controllers import EmailsController
from src.app.tasks.emails_tasks import send_email_task
from flask import jsonify


prefix = '/api/emails'
emails = Blueprint('emails', __name__, url_prefix=prefix)
controller = EmailsController()

""" Get all emails, including sent and scheduled. """
@emails.route('', methods=['GET'])
def get_all_emails(): 
    status = request.args.get("status", default=None)
    # to = request.args.get("to", None)
    return controller.get_all_emails(status=status)

@emails.route("/<string:uuid_email>", methods = ["GET"])
def get_email_by_uuid(uuid_email: str): return controller.get_email_by_uuid(uuid_email)

"""  Route to send an e-mail """
@emails.route('/send', methods=['POST'])
def post_send_email(): return controller.send_email(request.get_json())

""" Route to send an schedule e-mail """
@emails.route('/schedule', methods=['POST'])
def post_schedule_email(): return controller.send_scheduled_email(request.get_json())

@emails.route('/schedule/<string:uuid_task>', methods=["DELETE"])
def delete_schedule_email(uuid_task): return controller.delete_schedule_email(uuid_task)
