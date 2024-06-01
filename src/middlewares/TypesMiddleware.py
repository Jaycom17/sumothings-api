from models.ProductTypeModel import ProductTypeModel

def typesMiddleware(Type):
    try:
        return ProductTypeModel(Type["ptName"])
    except KeyError as e:
        return None