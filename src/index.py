from flask import Flask
from config.config import config
from database.database import configure_database
from database.database import db

# Routes
from routes.DealersRoutes import setupRoutesDealer
from routes.ShoppingsRoutes import setupRoutesShopping

app = Flask(__name__)

def init_app(config):
    # Configuration
    app.config.from_object(config)

    configure_database(app)
    setupRoutesDealer(app)
    setupRoutesShopping(app)

    return app

configuration = config['development']
app = init_app(configuration)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()