from flask import Blueprint

profiles_frontend = Blueprint('profiles_frontend', __name__, url_prefix="")

@profiles_frontend.get("/me")
def views_my_profile():
    return None
