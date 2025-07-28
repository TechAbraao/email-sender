from flask import Flask
from src.app.blueprints.routes.emails_routes import emails
from celery import Celery

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(emails)
      
    return app

if __name__ == '__main__':
    app = create_app()
    celery_app = Celery("email_sender", broker="amqp://guest:guest@localhost:5672//", backend="rpc://")
    app.run(debug=True) 