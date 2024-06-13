from models.ShoppingModel import ShoppingModel, ShoppingModelToUpdate
import uuid

def postShoppingMiddleWare(shopping):
    try:
        
        shoppings = []

        shoReceipt = str(uuid.uuid4())

        for product in shopping["products"]:
            shoppings.append(ShoppingModel(product["proID"], product["deaID"], shoReceipt, shopping["shoDate"], product["shoProductUnits"], product["shoPrice"], product["shoTaxes"]))

        return shoppings
    except KeyError as e:
        return None
    
def putShoppingMiddleWare(shopping, shoId):
    try:
        
        shoppings = []
        
        for product in shopping["products"]:
            shoppings.append(ShoppingModelToUpdate(product["shoID"], product["proID"], product["deaID"], shoId, shopping["shoDate"], product["shoProductUnits"], product["shoPrice"], product["shoTaxes"]))

        return shoppings
    except KeyError as e:
        print(e)
        return None