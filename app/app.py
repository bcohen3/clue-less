import logging

from flask import Flask, request as req
from flask_wtf.csrf import CSRFProtect

from app.server.api.resources import home
from config.app_configuration import SECRET_KEY


def create_app(config_filename):
    app = Flask(__name__, static_folder='client/static')

    app.config.from_object(config_filename)
    app.config['SECRET_KEY'] = SECRET_KEY

    app.register_blueprint(home.blueprint)

    app.logger.setLevel(logging.ERROR)

    csrf = CSRFProtect()
    csrf.init_app(app)

    @app.after_request
    def log_response(resp):
        app.logger.info("{} {} {}\n{}".format(
            req.method, req.url, req.data, resp)
        )
        return resp

    return app
