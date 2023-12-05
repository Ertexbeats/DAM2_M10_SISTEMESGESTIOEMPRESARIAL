from proven.friends.model.Friend import Friend
from proven.friends.views.FriendMenu import FriendMenu


class FriendView:
    def __init__( self, control, model ):
        self.control = control
        self.model = model
        self.menu = FriendMenu()

    def showInputDialog( self, message ):
        return input(message)

    def showMessage( self, message ):
        print( message )

    def display( self ):
        while True:
            self.menu.show()
            action = self.menu.getSelectedOptionActionCommand()
            self.processAction( action )

    def processAction( self, action ):
        if action is not None:
            self.control.processRequest( action )

    def showFriendTable( self, data ):
        for elem in data:
            print( elem )
        print( f"{len( data )} elements found" )

    def friendForm(self, input_friend):
        if input_friend is not None:
            print(str(input_friend))
        else:
            try:
                phone = self.showInputDialog("Input phone: ")
                name = self.showInputDialog("Input name: ").capitalize()
                age = self.showInputDialog("Input age: ")
                f = Friend(phone, name, age)
            except ValueError:
                return None
            except EOFError:
                return None
            return f


