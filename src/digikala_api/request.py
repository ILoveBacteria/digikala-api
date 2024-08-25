import requests
from digikala_api.product import Product


def product_detail(product_id: str) -> Product:
    """
    This function get product detail from digikala api

    Args:
        product_id (str): product id like: 15902244

    Returns:
        Product: A Product object that contains product detail
    """
    url = f'https://api.digikala.com/v2/product/{product_id}/'
    response = requests.get(url)
    return response.json()