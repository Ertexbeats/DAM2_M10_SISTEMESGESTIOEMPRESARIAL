from proven.shopping.views.Menu import Menu
from proven.shopping.views.Option import Option


class ShoppingMenu(Menu):
    def __init__(self):
        super().__init__("Shopping cart main menu")
        self.addOption(Option("Exit", "exit"))
        self.addOption(Option("Buy a product", "buy_a_product"))
        self.addOption(Option("Show purchased products", "show_purchased_products"))
        self.addOption(Option("Generate bill", "generate_bill"))
