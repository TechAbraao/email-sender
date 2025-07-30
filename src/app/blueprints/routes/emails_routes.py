from flask import Blueprint, request
from src.app.controllers.emails_controllers import EmailsController
from src.app.tasks.emails_tasks import send_email_task
from flask import jsonify


prefix = '/api/emails'
emails = Blueprint('emails', __name__, url_prefix=prefix)
controller = EmailsController()

"""  Route to send an e-mail """
@emails.route('/send', methods=['POST'])
def post_send_email(): return controller.send_email(request.get_json())

""" Route to send an schedule e-mail """
@emails.route('/schedule', methods=['POST'])
def get_schedule_email(): return controller.send_scheduled_email(request.get_json())

@emails.route('/schedule', methods=['POST'])
def post_schedule_email():
    """ Route to schedule an e-mail (not implemented yet) """
    return {"message": "This feature is not implemented yet"}, 501


