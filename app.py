from flask import Flask
from config import Config
from models import db
from routes import api
from seed import seed
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(api)
    app.register_blueprint(seed)

    jwt = JWTManager(app)

    # Creating tables in DB
    with app.app_context():
        db.create_all()
        
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)