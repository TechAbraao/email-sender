from flask import Blueprint, render_template, redirect, url_for, request

emails_frontend = Blueprint('emails_frontend', __name__, "/")


@emails_frontend.get("/")
def views_root():
    return redirect(url_for("emails_frontend.views_emails_sender"))


@emails_frontend.get("/emails")
def views_emails_sender():
    rendering_strategy = {"url": f"{request.path}"}
    return render_template("pages/send_emails.jinja2", strategy=rendering_strategy)


@emails_frontend.get("/history")
def views_email_history():
    rendering_strategy = {"url": f"{request.path}"}
    return render_template("pages/emails_history.jinja2", strategy=rendering_strategy)


@emails_frontend.get("/providers")
def views_configure_providers():
    rendering_strategy = {"url": f"{request.path}"}
    return render_template("pages/configure_providers.jinja2", strategy=rendering_strategy)


@emails_frontend.get("/me")
def views_my_profile():
    return None
