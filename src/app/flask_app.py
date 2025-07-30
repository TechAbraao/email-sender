from flask import Flask
from src.app.blueprints.routes.emails_routes import emails

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(emails)
    return app

if __name__ == '__main__':
    try:
        app = create_app()
        app.run(debug=True) 
    except Exception as e:
        print(f"\n [ERRO] Failed to initialize Flask App: \n [ERRO] {e} \n")
