from handlers import *
from flask import Flask
import config as cfg
import json


def create_flask_app(app_cfg):

    app = Flask(__name__)
    app.config.from_object(app_cfg)

    @app.route('/health')
    def hello():
        return status_hadnler(app)
    
    return app