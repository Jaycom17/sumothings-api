from models.SalesModel import SalesModel, SalesModelToUpdate
import uuid

def postSalesMiddleWare(sale_data):
    try:
        
        sales = []
        
        salReceipt = str(uuid.uuid4())
        
        for product in sale_data["products"]:
            sales.append(SalesModel(product["proID"], product["cliID"], salReceipt, sale_data["salDate"], product["salProductUnits"], product["salPrice"], product["salTaxes"]))
        
        return sales
    except KeyError as e:
        return None

def putSalesMiddleWare(sale, salId):
    try:
        
        sales = []
        
        for product in sale["products"]:
            sales.append(SalesModelToUpdate(product["salID"], product["proID"], product["cliID"], salId, sale["salDate"], product["salProductUnits"], product["salPrice"], product["salTaxes"]))

        return sales
    except KeyError as e:
        print(e)
        return None
