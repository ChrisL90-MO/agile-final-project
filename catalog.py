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

def update_product(product_id, name, description, price):
    """Update an existing product in the catalog."""
    if product_id in products:
        products[product_id]["name"] = name
        products[product_id]["description"] = description
        products[product_id]["price"] = price
        return products[product_id]
    return None
def delete_product(product_id):
    """Delete a product from the catalog."""
    if product_id in products:
        del products[product_id]
        return True
    return False
