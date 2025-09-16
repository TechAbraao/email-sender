from flask import Blueprint

prefix = ""
providers = Blueprint("providers", __name__, url_prefix=prefix)