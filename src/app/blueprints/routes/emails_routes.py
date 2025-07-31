from flask import Blueprint, request
from src.app.controllers.emails_controllers import EmailsController
from src.app.tasks.emails_tasks import send_email_task
from flask import jsonify
import logging

prefix = '/api/emails'
emails = Blueprint('emails', __name__, url_prefix=prefix)
controller = EmailsController()
logger = logging.getLogger(__name__)

""" Get all emails, including sent and scheduled. """
@emails.route('', methods=['GET'])
def get_all_emails():
    logger.info(f"\033[93m[GET] /emails\033[0m")
    status = request.args.get("status", default=None)
    # to = request.args.get("to", None)
    return controller.get_all_emails(status=status)

@emails.route("/<string:uuid_email>", methods = ["GET"])
def get_email_by_uuid(uuid_email: str):
    return controller.get_email_by_uuid(uuid_email)

"""  Route to send an e-mail """
@emails.route('/send', methods=['POST'])
def post_send_email():
    logger.info(f"\033[93m[POST] /emails/send\033[0m")
    return controller.send_email(request.get_json())

""" Route to send an schedule e-mail """
@emails.route('/schedule', methods=['POST'])
def post_schedule_email():
    logger.info(f"\033[93m[POST] /emails/schedule\033[0m")
    return controller.send_scheduled_email(request.get_json())

@emails.route('/schedule/<string:uuid_task>', methods=["DELETE"])
def delete_schedule_email(uuid_task):
    logger.info(f"\033[93m[DELETE] /emails/schedule/{uuid_task}\033[0m")
    return controller.delete_schedule_email(uuid_task)
