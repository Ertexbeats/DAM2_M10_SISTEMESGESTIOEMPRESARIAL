import sys, os

from proven.manage.views.FileView import FileView
from proven.manage.model.File import File
from proven.manage.model.FileModel import FileModel


class FileController:
    def __init__(self, model: FileModel):
        self.model = model
        self.view = FileView(self, model)
        self.view.display()

    def processRequest(self, action):
        if action is None:
            action = "wrong_action"
        if action == "exit":
            self.exit_application()
        elif action == "create_a_file":
            self.createFile()
        elif action == "read_content_file":
            self.readFile()
        elif action == "write_to_a_file":
            self.writeFile()
        elif action == "delete_a_file":
            self.deleteFile()
        elif action == "wrong_action":
            self.view.showMessage("Wrong option")

    def exit_application(self):
        sys.exit(0)

    def inputFileName(self, message):
        self.model.saveFileName(self.view.inputFileName(message))
        filePath = f"proven/resources/{self.model.readFileName()}"
        return filePath

    def inputDataToFile(self, message):
        return self.view.inputDataToFile(message)

    def createFile(self):
        filename = self.inputFileName("Enter the name of the file to create: ")
        file = open(filename, "w")
        file.close()

    def readFile(self):
        try:
            filename = self.inputFileName("Enter the name of the file to read: ")
            fich_ent = open(filename, "r")
            for linea in fich_ent:
                print(linea)
            fich_ent.close()
        except FileNotFoundError:
            print(f"Oops! this file {filename} doesn't exist. Try again...")

    def writeFile(self):
        filename = self.inputFileName("Enter the name of the file to write: ")
        file = open(filename, "w")
        dataToWrite = self.inputDataToFile("Enter the data to write: ")
        file.write(dataToWrite)
        file.close()

    def deleteFile(self):
        try:
            filename = self.inputFileName("Enter the name of the file to delete: ")
            if filename is not None:
                os.remove(filename)
                print("File deleted successfully")
        except FileNotFoundError:
            print(f"Oops! this file {filename} doesn't exist. Try again...")
