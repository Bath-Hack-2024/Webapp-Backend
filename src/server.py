from handlers import *
from flask import Flask
import config as cfg
import json

from flask_cors import CORS, cross_origin


def create_flask_app(app_cfg):

    app = Flask(__name__)
    app.config.from_object(app_cfg)

    @app.route('/health')
    @cross_origin()
    def hello():
        return status_hadnler(app)
    
    @app.route('/register_station', methods=['POST'])
    @cross_origin()
    def register_station():
        return register_station_handler(app)
    
    @app.route('/upload-data', methods=['POST'])
    @cross_origin()
    def upload_data():
        return upload_data_handler(app)
    
    @app.route('/upload-image', methods=['POST'])
    @cross_origin()
    def upload_image():
        return upload_image_handler(app)
    
    return app