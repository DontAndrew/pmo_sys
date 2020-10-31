from .config import ProdConfig, DevConfig
from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    if os.environ.get("ENV") == "production":
        app.config.from_object(ProdConfig)
    else:
        app.config.from_object(DevConfig)

    from .routes import main

    app.register_blueprint(main)

    return app
