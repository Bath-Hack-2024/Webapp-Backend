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
    
    @app.route('/register_station', methods=['POST'])
    def register_station():
        return register_station_handler(app)
    
    @app.route('/upload-data', methods=['POST'])
    def upload_data():
        return upload_data_handler(app)
    
    return app