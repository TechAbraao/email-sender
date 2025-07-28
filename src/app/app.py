from flask import Flask
from src.app.blueprints.routes.emails_routes import emails
from celery import Celery
from src.app.settings.rabbitmq_settings import RabbitMQSettings

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(emails)
    return app

rabbit_settings = RabbitMQSettings()
if __name__ == '__main__':
    try:
        app = create_app()
        celery_app = Celery(
            {rabbit_settings.name}, 
            broker=f"amqp://{rabbit_settings.user}:{rabbit_settings.password}@{rabbit_settings.host}:{rabbit_settings.port}//", 
            backend=rabbit_settings.backend
            )
        app.run(debug=True) 
    except Exception as e:
        print(f"\n [ERRO] Failed to initialize server: \n [ERRO] {e} \n")
