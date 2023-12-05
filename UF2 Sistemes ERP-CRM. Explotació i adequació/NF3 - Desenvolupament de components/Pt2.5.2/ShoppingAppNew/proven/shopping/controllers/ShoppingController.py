import sys, os

from proven.shopping.views.ShoppingView import ShoppingView
from proven.shopping.model.Product import Product
from proven.shopping.model.ShoppingModel import ShoppingModel
from proven.shopping.model.Bill import Bill


class ShoppingController:
    def __init__(self, model: ShoppingModel):
        self.model = model
        self.view = ShoppingView(self, model)
        self.view.display()

    def processRequest(self, action):
        if action is None:
            action = "wrong_action"
            self.view.showMessage("Wrong option")

        if action == "exit":
            self.exitApplication()

        elif action == "buy_a_product":
            self.buyProduct()

        elif action == "show_purchased_products":
            self.showPurchasedProducts()

        elif action == "generate_bill":
            self.generateBill()

        else:
            self.view.showMessage("Wrong option")

    def exitApplication(self):
        sys.exit(0)

    def buyProduct(self):
        self.model.showProducts()
        try:
            opcion = int(self.view.showInputDialog("Input product: "))

            if opcion >= 0 & opcion < len(self.model.products):
                result = self.model.shoppingCart(opcion)

                if result:
                    self.view.showMessage("Product add to ShoppingCart")
                else:
                    self.view.showMessage("Product not add to ShoppingCart")

            else:
                self.view.showMessage("Wrong option")

        except ValueError:
            self.view.showMessage("Only numbers please")
        except Exception:
            self.view.showMessage("Error processing request")

    def showPurchasedProducts(self):
        self.model.showProductsCart()

    def generateBill(self):
        shoppinCart = self.model.showCart()

        if shoppinCart is not None:
            dni = self.billInputDni()
            name = self.billInputName()
            surname = self.billInputSurname()
            phone = self.billInputPhone()
            totalPrice = self.billInputTotalPrice()
            billToGenerate = Bill(dni, name, surname, phone, totalPrice)

            if billToGenerate is not None:
                self.view.showMessage("Bill Generated")
                print(billToGenerate)
                answer = self.view.showInputDialog("Delete Cart? (s/n): ").lower()
                if answer.__eq__("s"):
                    self.model.clearCart()
                    self.view.showMessage("Cart deleted")
                elif answer.__eq__("n"):
                    self.view.showMessage("Cart not deleted")
                else:
                    self.view.showMessage("error processing request")

        else:
            self.view.showMessage("Add products in the Shopping cart")

    def billInputDni(self):
        while True:
            dni = self.view.showInputDialog("DNI: ")
            dni = dni.strip()

            if dni.isdigit() and len(dni) == 8:
                return dni
            else:
                print("Invalid DNI")

    def billInputName(self):
        while True:
            name = self.view.showInputDialog("Name: ")
            name = name.strip()

            if name.isalpha():
                return name
            else:
                print("Invalid Name")

    def billInputSurname(self):
        while True:
            surname = self.view.showInputDialog("Surname: ")
            surname = surname.strip()

            if surname.isalpha():
                return surname
            else:
                print("Invalid Surname")

    def billInputPhone(self):
        while True:
            phone = self.view.showInputDialog("Phone: ")
            phone = phone.strip()

            if phone.isdigit() and len(phone) == 9:
                return phone
            else:
                print("Invalid Phone")

    def billInputTotalPrice(self):
        totalPrice = self.model.totalPrice()
        return totalPrice
