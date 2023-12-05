class File:
    def __init__(self, filename=None):
        self.filename = filename

    def getFilename(self):
        return str(self.filename)

    def setFilename(self, filename):
        self.filename = filename

    def __str__(self):
        return f"File{{Filename={self.filename}}}"
