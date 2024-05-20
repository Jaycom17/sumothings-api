from models.ProductModel import ProductModel

def productMiddleWare(product):
    try:
        return ProductModel(product["proID"], product["proName"], product["proStock"], product["proHeight"], product["proWidth"], product["proLength"], product["proWeight"], product["proBuyPrice"], product["proSellPrice"], product["proMinStock"], product["proMaxStock"], product["proDescription"], product["proImage"], product["proTypeID"])
    except KeyError as e:
        return None



