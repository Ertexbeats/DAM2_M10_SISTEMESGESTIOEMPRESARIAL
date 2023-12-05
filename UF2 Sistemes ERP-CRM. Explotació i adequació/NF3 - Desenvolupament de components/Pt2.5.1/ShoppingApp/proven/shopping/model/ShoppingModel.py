from proven.shopping.model.Product import Product
from proven.shopping.model.Shop import Shop


class ShoppingModel:
    def __init__(self):
        self.shop = Shop()
        self.products = self.shop.products
        self.productsCart = self.shop.productsCart

    def findAllProducts(self):
        return self.products

    def showProducts(self):
        listproductos = self.products
        for i in range(len(listproductos)):
            print(f"[{i}] {listproductos[i].__str__()}")

    def findProductByName(self, name):
        products = None
        if name is not None and isinstance(name, str):
            all_products = self.findAllProducts()
            products = []
            for product in all_products:
                if (
                    isinstance(product.productName, str)
                    and product.productName.lower() == name.lower()
                ):
                    products.append(product)
        return products

    def shoppingCart(self, posicion):
        product = self.products[posicion]
        if product.quantity == 0:
            return False
        if self.addProductToShopping(product, product.quantity):
            product.quantity -= 1
            return True
        else:
            print("Failed to add product to shopping cart.")
            return False

    def addProductToShopping(self, product, quantity):
        try:
            product_names = [p.getProductName() for p in self.productsCart]
            if product.getProductName() in product_names:
                productCart = next(
                    p
                    for p in self.productsCart
                    if p.getProductName() == product.getProductName()
                )
                productCart.setQuantity(productCart.getQuantity() + 1)
            else:
                quantityInCart = (quantity + 1) - product.getQuantity()
                productCart = Product(
                    product.getProductName(), product.getPrice(), quantityInCart
                )
                self.productsCart.append(productCart)
            return True
        except Exception:
            return False

    def clearCart(self):
        self.__init__()

    def showProductsCart(self):
        listproductos = self.productsCart
        for i in range(len(listproductos)):
            print(f"[{i}] {listproductos[i].__str__()}")

    def showCart(self):
        if len(self.productsCart) > 0:
            return self.productsCart
        else:
            return None

    def totalPrice(self):
        total = 0
        for product in self.productsCart:
            total += product.getPrice() * product.getQuantity()
        return total
