from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class EmailSettings:
    """Class to hold email settings."""
    smtp_server: str = os.getenv("SMTP_SERVER")
    smtp_port: int = os.getenv("SMTP_PORT", 587)
    smtp_email: str = os.getenv("SMTP_EMAIL")
    smtp_password: str = os.getenv("SMTP_PASSWORD")
