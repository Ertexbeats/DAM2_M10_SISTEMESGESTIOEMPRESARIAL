from proven.manage.model.File import File


class FileModel:
    def __init__(self):
        self.file = File()

    def readFileName(self):
        return self.file.getFilename()

    def saveFileName(self, fileName):
        self.file.setFilename(fileName)
