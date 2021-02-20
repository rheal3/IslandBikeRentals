from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
# migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.app_config")

    db.init_app(app)
    ma.init_app(app)
    # migrate.init_app(app, db)

    # from commands import db_commands
    # app.register_blueprint(db_commands)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    

    return app
