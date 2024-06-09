from flask import Flask
from config.config import config
from database.database import configure_database
from database.database import db

# Routes
from routes.DealersRoutes import setupRoutesDealer
from routes.ShoppingsRoutes import setupRoutesShopping
from routes.ProductsRoutes import setupRoutesProduct
from routes.ArticlesRoutes import setupRoutesArticle

# CORS
from flask_cors import CORS

# SWAGGER
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

def init_app(config):

    # Swagger
    SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = '/static/openapi.json'  # Our API url (can of course be a local resource)

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Test application"
        },
        # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        #    'clientId': "your-client-id",
        #    'clientSecret': "your-client-secret-if-required",
        #    'realm': "your-realms",
        #    'appName': "your-app-name",
        #    'scopeSeparator': " ",
        #    'additionalQueryStringParams': {'test': "hello"}
        # }
    )

    app.register_blueprint(swaggerui_blueprint)

    # Configuration
    app.config.from_object(config)

    configure_database(app)
    setupRoutesDealer(app)
    setupRoutesShopping(app)
    setupRoutesProduct(app)
    setupRoutesArticle(app)

    CORS(app)

    return app

configuration = config['development']
app = init_app(configuration)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()