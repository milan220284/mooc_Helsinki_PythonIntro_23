
def search(products: list, criterion: callable):
    
    return [x for x in products if criterion(x)]
