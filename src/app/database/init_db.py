from src.app.database.configs_database import Base, engine
from src.app.models.emails_model import EmailsModel

def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        print("\n [INFO] Database tables created (or already exist).")
        print(" [INFO] Existing tables: ")
        for table in Base.metadata.tables.keys():
            print(" *", table)
    except Exception as e:
        print(f"\n [ERRO] Failed to initialize database: \n [ERRO] {e} \n")
