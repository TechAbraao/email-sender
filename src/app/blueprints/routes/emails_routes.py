from flask import Blueprint, request
from src.app.controllers.emails_controllers import EmailsController

prefix = '/api/emails'
emails = Blueprint('emails', __name__, url_prefix=prefix)
controller = EmailsController()

"""  Route to send an e-mail """
@emails.route('/send', methods=['POST'])
def post_send_email(): return controller.send_email(request.get_json())

@emails.route('/schedule', methods=['GET'])
def get_schedule_email():
    """ Route to get scheduled e-mails (not implemented yet) """
    return {"message": "This feature is not implemented yet"}, 501

@emails.route('/schedule', methods=['POST'])
def post_schedule_email():
    """ Route to schedule an e-mail (not implemented yet) """
    return {"message": "This feature is not implemented yet"}, 501


