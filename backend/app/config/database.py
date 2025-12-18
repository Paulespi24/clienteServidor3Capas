"""
Configuración de la base de datos - Tier 3: Acceso a Datos
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    """Inicializa la base de datos"""
    db.init_app(app)
    with app.app_context():
        db.create_all()


