from flask import Blueprint, render_template, redirect, url_for

emails_frontend = Blueprint(
    'emails_frontend',
    __name__,
    "/"
)

@emails_frontend.get("/")
def views_root():
    return redirect(url_for("emails_frontend.views_emails_sender"))

@emails_frontend.get("/emails")
def views_emails_sender():
    return render_template("pages/send_emails.jinja2")

@emails_frontend.get("/history")
def views_email_history():
    return render_template("pages/email_history.jinja2")

@emails_frontend.get("/providers")
def views_configure_providers():
    return render_template("pages/configure_providers.jinja2")
