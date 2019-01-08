from flask import Flask, Blueprint
from instance.config import app_config
from .api.v1 import v1 as version_1


def create_app(config_name="development"):
    app = Flask("__name__", instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    app.register_blueprint(version_1)
    return app