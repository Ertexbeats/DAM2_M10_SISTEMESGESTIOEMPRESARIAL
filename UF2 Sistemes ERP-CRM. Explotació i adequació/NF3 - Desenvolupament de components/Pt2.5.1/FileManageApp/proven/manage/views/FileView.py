from proven.manage.views.FileMenu import FileMenu
from proven.manage.model.File import File


class FileView:
    def __init__(self, control, model):
        self.control = control
        self.model = model
        self.menu = FileMenu()

    def showInputDialog(self, message):
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

    def inputFileName(self, message):
        return self.showInputDialog(message)

    def inputDataToFile(self, message):
        return self.showInputDialog(message)
