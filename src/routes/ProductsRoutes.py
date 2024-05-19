from flask import Blueprint, jsonify
from services.ProductsServices import ProductsServices

import traceback

main = Blueprint('products', __name__)

@main.route('/', methods=['GET'])
def get_products():
    try:
        return jsonify(ProductsServices.get_products())
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()})