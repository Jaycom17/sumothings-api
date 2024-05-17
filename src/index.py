from flask import Flask
from config.config import config

# Routes
from routes import ProductsRoutes

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(ProductsRoutes.main, url_prefix='/products')
    #app.register_blueprint(AuthRoutes.main, url_prefix='/auth')
    #app.register_blueprint(LanguageRoutes.main, url_prefix='/languages')

    return app

configuration = config['development']
app = init_app(configuration)

if __name__ == '__main__':
    app.run()