from proven.manage.controllers.FileController import FileController
from proven.manage.model.FileModel import FileModel


class ManageFilesApp:
    def run(self):
        FileController(FileModel())


main = ManageFilesApp()
main.run()
