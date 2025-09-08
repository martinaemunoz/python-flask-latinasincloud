from flask import Flask

# # versión simple
# app = Flask(__name__)

# @app.route('/') # /hola
# def hello_world():
#     return 'Hola Flask! Versión simple'

# Renderizar HTML5
def create_app():
    app = Flask(__name__)

    # Importar rutas
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app