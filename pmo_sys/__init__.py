from pmo_sys.config import ProdConfig, DevConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    if os.environ.get("ENV") == "production":
        app.config.from_object(ProdConfig)
    else:
        app.config.from_object(DevConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main

    app.register_blueprint(main)

    return app
