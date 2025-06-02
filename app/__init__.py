from flask import Flask
from .modules.marca.marca_routes import marca_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(marca_bp)
    return app