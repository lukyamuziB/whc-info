from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config


bootstrap = Bootstrap()
moment = Moment()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config['development'])
    config['development'].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)

    """Register blueprints"""

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

