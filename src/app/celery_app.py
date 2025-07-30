from celery import Celery
from src.app.settings.rabbitmq_settings import RabbitMQSettings

try:
    rabbit_settings = RabbitMQSettings()
    celery_app = Celery(
            namespace="celery", 
            broker=f"amqp://{rabbit_settings.user}:{rabbit_settings.password}@{rabbit_settings.host}:{rabbit_settings.port}//", 
            backend=rabbit_settings.backend,
            include=["src.app.tasks.emails_tasks"]
            )
except Exception as e:
    print(f"\n [ERRO] Failed to initialize Celery App: \n [ERRO] {e} \n")