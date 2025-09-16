from flask import Flask
from src.app.blueprints.api.emails_routes import emails
from flask_migrate import Migrate
from src.app.settings.database_settings import postgres_settings
from src.app.logs.setup_logger import setup_logging
from src.app.utils.extesions import *

def create_app() -> Flask:
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = postgres_settings.get_uri()

    setup_logging()

    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db, directory="src/migrations")

    # Entities
    from src.app.models.emails_model import EmailsModel

    app.register_blueprint(emails)
    return app

if __name__ == '__main__':
    try:
        app = create_app()
        app.run(debug=True) 
    except Exception as e:
        print(f"\n [ERRO] Failed to initialize Flask App: \n [ERRO] {e} \n")
