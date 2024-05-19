from models.ShoppingModel import ShoppingModel

def shoppingMiddleWare(shopping):
    try:
        return ShoppingModel(shopping["proID"], shopping["deaID"], shopping["shoReceipt"], shopping["shoDate"], shopping["shoProductUnits"], shopping["shoPrice"], shopping["shoTaxes"])
    except KeyError as e:
        return None