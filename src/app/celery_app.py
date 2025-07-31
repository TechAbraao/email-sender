from celery import Celery
from src.app.settings.rabbitmq_settings import RabbitMQSettings
from kombu import Exchange, Queue

try:
    rabbit_settings = RabbitMQSettings()
    celery_app = Celery(
            namespace="celery", 
            broker=f"amqp://{rabbit_settings.user}:{rabbit_settings.password}@{rabbit_settings.host}:{rabbit_settings.port}//", 
            backend=rabbit_settings.backend,
            include=["src.app.tasks.emails_tasks"]
            )
    
    # Settings to ensure persistence
    email_exchange = Exchange(
        name="emails",
        type="direct",
        durable=True
    )
    email_queue = Queue(
        "emails",
        exchange=email_exchange,
        routing_key="emails",
        durable=True
    )
    
    celery_app.conf.task_queues = (email_queue,)

    celery_app.conf.task_default_queue = "emails"
    celery_app.conf.task_default_exchange = "emails"
    celery_app.conf.task_default_exchange_type = "direct"
    celery_app.conf.task_default_routing_key = "emails"

    celery_app.conf.task_default_delivery_mode = "persistent" 

    
except Exception as e:
    print(f"\n [ERRO] Failed to initialize Celery App: \n [ERRO] {e} \n")