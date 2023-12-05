from proven.manage.views.Menu import Menu
from proven.manage.views.Option import Option


class FileMenu(Menu):
    def __init__(self):
        super().__init__("Gestion Manager main menu")
        self.addOption(Option("Exit", "exit"))  # Funciona
        self.addOption(Option("Create a file", "create_a_file"))
        self.addOption(Option("Read the contents of a file", "read_content_file"))
        self.addOption(Option("Write to a file", "write_to_a_file"))
        self.addOption(Option("Delete a file", "delete_a_file"))
