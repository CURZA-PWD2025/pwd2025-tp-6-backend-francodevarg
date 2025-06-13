from flask import Flask
from .modules.articulo.articulo_routes import articulo_bp
from .modules.categoria.categoria_routes import categoria_bp
from .modules.proveedor.proveedor_routes import proveedor_bp
from .modules.marca.marca_routes import marca_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(articulo_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(marca_bp)
    app.register_blueprint(proveedor_bp)
    return app