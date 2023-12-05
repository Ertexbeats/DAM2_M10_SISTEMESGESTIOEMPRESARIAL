from proven.friends.controllers.FriendController import FriendController
from proven.friends.model.FriendModel import FriendModel


class FriendApp:
    def run( self ):
        FriendController( FriendModel() )


main = FriendApp()
main.run()
