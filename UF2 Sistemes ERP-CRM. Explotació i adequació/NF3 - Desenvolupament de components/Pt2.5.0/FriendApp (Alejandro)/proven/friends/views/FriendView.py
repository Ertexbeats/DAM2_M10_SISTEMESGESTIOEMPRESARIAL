from proven.friends.views.FriendMenu import FriendMenu
from proven.friends.model.Friend import Friend


class FriendView:
    def __init__(self, control, model):
        self.control = control
        self.model = model
        self.menu = FriendMenu()

    def shoInputDialog(self, message):
        return str(input(message))

    def showMessage(self, message):
        print(message)

    def display(self):
        while True:
            self.menu.show()
            action = self.menu.getSelectOptionActionCommand()
            self.processAction(action)

    def processAction(self, action):
        if action is not None:
            self.control.processRequest(action)

    def showFriendTable(self, data):
        for friend in data:
            print(str(friend))
        print(f"{data.__len__()} elements found")

    def friendForm(self, input_friend):
        if input_friend is not None:
            print(str(input_friend))
        else:
            try:
                while True:
                    phone = self.shoInputDialog("Input phone: ")
                    if self.phoneForm(phone) is not False:
                        break
                while True:
                    name = self.shoInputDialog("Input name: ").capitalize()
                    if self.nameForm(name) is not False:
                        break
                while True:
                    age = self.shoInputDialog("Input age: ")
                    if self.ageForm(age) is not False:
                        break
                f = Friend(phone, name, age)
            except ValueError:
                return None
            except EOFError:
                return None
            return f

    def phoneForm(self, phone):
        if phone.__len__() == 9:
            if phone.isdigit():
                return True
            else:
                print("The telephone should be numbers")
                return False
        else:
            print("The telephone number must be 9 digits long")
            return False

    def nameForm(self, name):
        if name.isalpha():
            return True
        else:
            print("The name must have only letters")
            return False

    def ageForm(self, age):
        if age.isdigit():
            if 0 < int(age) < 120:
                return True
            else:
                print("The age must be a positive number and less than 120.")
                return False
        else:
            print("The age must be a number")
            return False
