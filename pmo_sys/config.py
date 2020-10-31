import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class ProdConfig(Config):
    ENV = "production"
    pass


class DevConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True
