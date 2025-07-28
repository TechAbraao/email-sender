from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class RabbitMQSettings:
    """ Broker settings for RabbitMQ. """
    host: str = os.getenv("RABBITMQ_DEFAULT_HOST", "localhost")
    port: int = int(os.getenv("RABBITMQ_DEFAULT_PORT"))
    user: str = os.getenv("RABBITMQ_DEFAULT_USER")
    password: str = os.getenv("RABBITMQ_DEFAULT_PASS")
    name: str = os.getenv("RABBITMQ_DEFAULT_NAME")
    backend: str = "rpc://"