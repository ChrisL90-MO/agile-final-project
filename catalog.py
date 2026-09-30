products = {}


def create_product(product_id, name, description, price):
    """Create a new product in the catalog."""
    product = {
        "id": product_id,
        "name": name,
        "description": description,
        "price": price
    }

    products[product_id] = product
    return product

def get_product(product_id):
    """Retrieve a product from the catalog."""
    return products.get(product_id)
