from flask import Flask
from flask_cors import CORS

from config.config import config
from database.database import configure_database
from database.database import db
import os

# Routes
from routes.DealersRoutes import setupRoutesDealer
from routes.ShoppingsRoutes import setupRoutesShopping
from routes.SalesRoutes import setupRoutesSales
from routes.ProductsRoutes import setupRoutesProduct
from routes.ArticlesRoutes import setupRoutesArticle


# CORS

from routes.TypesRoutes import setupRoutesType
from routes.AdminUserRoutes import setupRoutesAdminUser
from routes.ClientsRoutes import setupRoutesClients
from routes.AuthRoutes import setupRoutesAuth
from routes.EmailRoutes import setupRoutesEmail
from flask_cors import CORS

# SWAGGER
from flask_swagger_ui import get_swaggerui_blueprint


#swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:4200"}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS, GET, PUT, DELETE')
    response.headers.add('X-DNS-Prefetch-Control', 'off')
    return response


UPLOAD_FOLDER = os.path.join(os.getcwd(),'images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def init_app(config):
<<<<<<< HEAD

    # Swagger
=======
>>>>>>> JoseBranch
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
<<<<<<< HEAD

=======
    
>>>>>>> JoseBranch
    # Configuration
    app.config.from_object(config)

    configure_database(app)
    setupRoutesDealer(app)
    setupRoutesShopping(app)
    setupRoutesSales(app)
    setupRoutesProduct(app)
    setupRoutesArticle(app)
    setupRoutesType(app)
    setupRoutesAdminUser(app)
    setupRoutesClients(app)
    setupRoutesAuth(app)
    setupRoutesEmail(app)

    CORS(app)

    return app

configuration = config['development']
app = init_app(configuration)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()