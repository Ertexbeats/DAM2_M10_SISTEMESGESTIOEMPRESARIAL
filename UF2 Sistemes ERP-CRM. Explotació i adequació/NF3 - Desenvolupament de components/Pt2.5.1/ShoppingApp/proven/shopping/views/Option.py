class Option:
    def __init__(self, text=None, action_command=None):
        self.text = text
        self.actionCommand = action_command

    def getText(self):
        return self.text

    def getActionCommand(self):
        return self.actionCommand

    def setText(self, text):
        self.text = text

    def setActionCommand(self, action_command):
        self.actionCommand = action_command

    def __eq__(self, __o):
        return super().__eq__(__o)

    def __hash__(self):
        return super().__hash__()

    def __str__(self):
        return f"Option{{text={self.text}, actionCommand={self.actionCommand}}}"
