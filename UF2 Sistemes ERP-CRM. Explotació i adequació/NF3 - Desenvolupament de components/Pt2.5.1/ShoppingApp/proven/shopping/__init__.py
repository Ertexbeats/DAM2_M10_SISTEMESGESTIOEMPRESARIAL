from proven.shopping.controllers.ShoppingController import ShoppingController
from proven.shopping.model.ShoppingModel import ShoppingModel


class ManageShoppingApp:
    def run(self):
        ShoppingController(ShoppingModel())


main = ManageShoppingApp()
main.run()
