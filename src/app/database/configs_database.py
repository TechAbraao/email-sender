from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.app.settings.database_settings import DatabaseSettings

c = DatabaseSettings()

try:
    DATABASE_URL: str = f"postgresql+psycopg2://{c.user}:{c.password}@{c.host}:{c.port}/{c.db_name}"
    engine = create_engine(DATABASE_URL, echo=False, pool_recycle=3600) # Create the database engine with connection pooling
    SessionLocal = sessionmaker(bind=engine) # Session factory for creating new sessions
    Base = declarative_base() # Base class for declarative models
except Exception as e:
    exit(f"\n [ERRO] Could not connect to database.\n [ERRO] Error: {e}\n")