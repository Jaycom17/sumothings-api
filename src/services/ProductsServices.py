import traceback

from database.database import get_connection


class ProductsServices:
    @staticmethod
    def get_products():
        try:
            connection = get_connection()
            products = None
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM products')
                products = cursor.fetchall()
            connection.close()
            return products
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return None