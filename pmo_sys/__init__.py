from .config import Config
from flask import Flask


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes import main

    app.register_blueprint(main)

    return app