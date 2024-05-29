from flask import Flask
import os
from src.routes import init_routes


def create_app():
    app = Flask(
        __name__, template_folder='templates', static_folder='views/static'
        )
    init_routes(app)
    return app


# @app.route("/")  # Cria uma rota, para a raiz do projeto. (GET por padrão)
# def hello_world():  # Método a ser executado ao navegar
#     return 'Hello World!'


if __name__ == '__main__':
    #  debug = True, reinicia automaticamente a cada mudança de arquivo
    #  mude a porta, caso ela estiver em uso
    app = create_app()
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
