from models.ShoppingModel import ShoppingModel
import uuid

def shoppingMiddleWare(shopping):
    try:
        
        shoppings = []

        shoReceipt = str(uuid.uuid4())

        for product in shopping["products"]:
            shoppings.append(ShoppingModel(product["proID"], shopping["deaID"], shoReceipt, shopping["shoDate"], product["proUnits"], product["proPrice"], product["proTaxes"]))

        return shoppings
    except KeyError as e:
        return None