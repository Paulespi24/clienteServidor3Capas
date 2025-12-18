"""
Punto de entrada de la aplicación - Tier 2: Lógica de Negocio
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


