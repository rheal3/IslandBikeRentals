import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "bluefishpurple"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.getenv("DATABASE_URL")

        if not value:
            raise ValueError("DATABASE_URL is not set!")
        
        return value

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.getenv("DB_URI_TEST")

        if not value:
            raise ValueError("DB_URI_TEST is not set!")
        
        return value

environment = os.getenv("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()