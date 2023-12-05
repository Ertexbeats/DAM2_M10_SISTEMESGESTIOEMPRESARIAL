class Menu:
    def __init__(self, title: str = None):
        self.title = title
        self.options = []

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getOption(self, index):
        return self.options[index]

    def addOption(self, option):
        return self.options.append(option)

    def removeOption(self, option):
        self.options.remove(option)

    def __str__(self):
        return f"Menu{{title={self.title}, options={self.options}}}"

    def show(self):
        print(f"------------ {self.title} ------------")
        for id_option, option in enumerate(self.options):
            print(f"[{id_option}] {option.getText()}")

    def getSelectedOption(self):
        try:
            opt = int(input("Select an option: "))
            if (opt < 0) or (opt >= len(self.options)):
                opt = -1
                print("Wrong option")
        except ValueError:
            opt = -1
        return opt

    def getSelectOptionActionCommand(self):
        option_number = self.getSelectedOption()
        if (option_number >= 0) and (option_number < len(self.options)):
            return self.options[option_number].getActionCommand()
        return None
