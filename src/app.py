
from server import create_flask_app
import config as cfg

if __name__ == '__main__':
    app = create_flask_app(cfg.app_config)
    app.run(host='0.0.0.0', debug=cfg.debug_mode, port=cfg.port)