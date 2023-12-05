from proven.shopping.model.Product import Product


class Shop:
    def __init__(self):
        self.products = []
        self.productsCart = []
        self.initProducts()

    def initProducts(self):
        self.products.append(Product("Doritos", 6.75, 2000))
        self.products.append(Product("Coca-Cola", 9.99, 2500))
        self.products.append(Product("Snickers", 7.50, 3000))
        self.products.append(Product("Cheetos", 4.50, 300))
        self.products.append(Product("Lavadora", 750, 150))
        self.products.append(Product("SmartTV", 1500, 3))
        self.products.append(Product("Play5", 500, 50))
        self.products.append(Product("Laptop", 955, 15))
