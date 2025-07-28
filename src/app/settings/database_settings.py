from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class DatabaseSettings:
    """Class to hold database settings."""
    host: str = os.getenv("DATABASE_HOST", "localhost")
    port: int = int(os.getenv("DATABASE_PORT", 5432))
    user: str = os.getenv("DATABASE_USER", "postgres")
    password: str = os.getenv("DATABASE_PASSWORD", "postgres")
    db_name: str = os.getenv("DATABASE_NAME", "emailsender")