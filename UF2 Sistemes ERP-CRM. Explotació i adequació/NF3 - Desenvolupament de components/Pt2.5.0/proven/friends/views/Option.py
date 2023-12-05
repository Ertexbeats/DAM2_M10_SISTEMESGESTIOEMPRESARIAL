class Option:
    def __init__( self, text, actionCommand ):
        self.text = text
        self.actionCommand = actionCommand

    def getText( self ):
        return self.text

    def setText( self, text ):
        self.text = text

    def getActionCommand( self ):
        return self.actionCommand

    def setActionCommand( self, actionCommand ):
        self.actionCommand = actionCommand

    def __hash__( self ):
        return super().__hash__()

    def __eq__( self, __o ):
        return super().__eq__( __o )

    def __str__( self ):
        return (f"Option: "
                f"text: {self.text}, "
                f"actionCommand: {self.actionCommand}")

# PRUEBAS
# optionPrueba = Option( "prueba1", "prueba" )
# print( optionPrueba )
# optionPrueba = Option( "prueba2", "prueba" )
# print( optionPrueba )
# optionPrueba = Option( "prueba3", "prueba" )
# print( optionPrueba )
