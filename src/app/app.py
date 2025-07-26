from flask import Flask
from src.app.blueprints.routes.emails import emails

def create_app():
    app = Flask(__name__)
    app.register_blueprint(emails)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) 