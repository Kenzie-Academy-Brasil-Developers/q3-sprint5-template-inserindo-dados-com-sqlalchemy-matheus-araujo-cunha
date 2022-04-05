from flask import Flask, Blueprint
from .salgado_blueprint import bp_salgados

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_salgados)

    app.register_blueprint(bp_api)
