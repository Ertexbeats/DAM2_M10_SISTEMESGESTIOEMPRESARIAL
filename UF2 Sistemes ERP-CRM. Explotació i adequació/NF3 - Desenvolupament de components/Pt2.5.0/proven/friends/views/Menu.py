class Menu:
    # CONSTRUCTOR
    def __init__( self, tittle: str = None):
        self.title = tittle
        self.options = []

    # GETTER & SETTERS
    def getTittle( self ):
        return self.title

    def setTittle( self, tittle ):
        self.title = tittle

    def getOptions( self, index ):
        return self.options.index( index )

    # METHODS
    def addOption( self, option ):
            return self.options.append( option )

    def removeOption( self, option ):
            self.options.remove( option )

    def removeOptionIndex( self, index ):
        if 0 <= index < len( self.options ):
            return self.options.remove( index )
        else:
            return None

    def __str__( self ):
        return (f"Menu: "
                f"tittle: {self.title}, "
                f"options: {self.options}")

    def show( self ):
        print( f"============ {self.title} ============" )
        for id_option, option in enumerate(self.options):
            print(f"[{id_option}] {option.getText()}")
        print( "==================================" )

    def getSelectedOption(self):
        try:
            opt = int(input("Select an option: "))
            if (opt < 0) or (opt >= len(self.options)):
                opt = -1
        except ValueError:
            opt = -1
        return opt

    def getSelectedOptionActionCommand(self):
        option_number = self.getSelectedOption()
        if (option_number >= 0) and (option_number < len(self.options)):
            return self.options[option_number].getActionCommand()
        return None
