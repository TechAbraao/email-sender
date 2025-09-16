from flask import Blueprint, render_template

emails_frontend = Blueprint(
    'emails_frontend',
    __name__,
    "/"
)

@emails_frontend.route("/", methods=["GET"])
def view_emails_sender():
    return render_template("pages/home.jinja2")