from models.SalesModel import SalesModel

class SalesMiddleware:
    @staticmethod
    def salesMiddleWare(sale_data):
        try:
            return SalesModel(
                sale_data["proID"],
                sale_data["cliID"],
                sale_data["salReceipt"],
                sale_data["salDate"],
                sale_data["salProductUnits"],
                sale_data["salPrice"],
                sale_data["salTaxes"]
            )
        except KeyError as e:
            return None
