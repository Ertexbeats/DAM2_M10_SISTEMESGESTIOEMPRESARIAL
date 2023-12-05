class Product:
    def __init__(self, productName=None, price=None, quantity=None):
        self.productName = productName
        self.price = price
        self.quantity = quantity

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
        return (
            f"Product: "
            f"Name: {self.productName}, "
            f"Price: {self.price}, "
            f"Stock: {self.quantity}"
        )
