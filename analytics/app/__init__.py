from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_restful import Api

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy()
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    return app
