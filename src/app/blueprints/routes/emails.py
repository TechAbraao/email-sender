from flask import Blueprint, request
from src.app.controllers.emails import EmailsController

emails = Blueprint('emails', __name__, url_prefix='/api/emails')
controller = EmailsController()

"""  Route to send an e-mail """
@emails.route('/send', methods=['POST'])
def send_email(): return controller.send_email(request.get_json())