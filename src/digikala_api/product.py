class Product:
    """
    This class represent a product in digikala
    
    Attributes:
        id (str): product id like: 15902244
        english_name (str): product english name
        persian_name (str): product persian name
        price (int): product price
        url (str): product url
        image_url (str): product image url
    """
    def __init__(self, id, english_name, persian_name, price, url, image_url):
        self.id = id
        self.english_name = english_name
        self.persian_name = persian_name
        self.price = price
        self.url = url
        self.image_url = image_url

    def __str__(self):
        return self.english_name

    def __repr__(self):
        return self.english_name
