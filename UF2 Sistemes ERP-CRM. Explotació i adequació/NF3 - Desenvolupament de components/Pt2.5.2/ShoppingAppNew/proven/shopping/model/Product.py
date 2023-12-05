class Product:

    def __init__(self, id_fab=None, id_producto=None, productName=None, price=None, quantity=None):
        # self.id_product = id_product
        self.id_fab = id_fab
        self.id_producto = id_producto
        self.productName = productName
        self.price = price
        self.quantity = quantity

    #    def getId_product(self):
    #        return self.id_product

    #    def setID_product(self, id_product):
    #        self.id_product = id_product

    def set_id_fab(self, id_fab):
        self.id_fab = id_fab

    def get_id_fab(self):
        return self.id_fab

    def set_id_product(self, id_producto):
        self.id_producto = id_producto

    def get_id_producto(self):
        return self.id_producto

    def getProductName(self):
        return self.productName

    def setProductName(self, productName):
        self.productName = productName

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return (f"\tProduct:\n"
                f"Id producto: {self.id_producto}\n"
                f"Name: {self.productName}\n"
                f"Price: {self.price}€\n"
                f"Stock: {self.quantity}\n")
