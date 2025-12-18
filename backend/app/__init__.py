"""
Aplicación Flask - Tier 2: Lógica de Negocio
Inicializa la aplicación y configura las rutas
"""
from flask import Flask, jsonify
from flask_cors import CORS
from app.config.database import init_db
from app.controllers.empresa_controller import empresa_bp
from app.controllers.servicio_controller import servicio_bp
from app.controllers.contrato_controller import contrato_bp

def create_app():
    """Factory function para crear la aplicación Flask"""
    app = Flask(__name__)
    
    # Configuración
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///limpieza_empresas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Habilitar CORS para comunicación con frontend
    CORS(app)
    
    # Inicializar base de datos
    init_db(app)
    
    # Registrar blueprints (rutas)
    app.register_blueprint(empresa_bp)
    app.register_blueprint(servicio_bp)
    app.register_blueprint(contrato_bp)
    
    @app.route('/')
    def index():
        return jsonify({'message': 'API de Servicios de Limpieza para Empresas', 'version': '1.0'})
    
    return app

