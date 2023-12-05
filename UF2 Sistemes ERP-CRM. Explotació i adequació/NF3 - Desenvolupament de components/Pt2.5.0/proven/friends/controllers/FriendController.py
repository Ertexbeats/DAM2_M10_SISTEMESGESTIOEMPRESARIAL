import sys

from proven.friends.model.Friend import Friend
from proven.friends.model.FriendModel import FriendModel
from proven.friends.views.FriendView import FriendView


class FriendController:
    def __init__( self, model: FriendModel ):
        self.model = model
        self.view = FriendView( self, model )
        self.view.display()

    def exitApplication( self ):
        sys.exit( 0 )

    def processRequest( self, action ):
        action = action if action is not None else "wrong_action"
        if action == "exit":
            self.exitApplication()
        elif action == "list_all_friends":
            self.listAllFriends()
        elif action == "search_friend_by_phone":
            self.searchFriendByPhone()
        elif action == "friend_form_remove":
            self.removeFriendForm()
        elif action == "friend_form_add":
            self.addFriend()
        elif action == "search_friends_by_name":
            self.searchFriendsByName()
        elif action == "friend_form_modify":
            self.modifyFriendForm()
        else:
            self.view.showMessage( "Wrong option" )

    def listAllFriends( self ):
        data = self.model.findAll()
        if data is not None:
            self.view.showFriendTable( data )
        else:
            self.view.showMessage( "Error retrieving data" )

    def searchFriendByPhone( self ):
        phone = self.view.showInputDialog( "Input phone: " )
        if phone is not None:
            friend = Friend( phone )
            found = self.model.find( friend )
            if found is not None:
                self.view.friendForm( found )
            else:
                self.view.showMessage( "Friend not found" )
        else:
            self.view.showMessage( "Error in parameter phone" )

    def searchFriendsByName( self ):
        name = self.view.showInputDialog( "Input name: " )
        if name is not None:
            data = self.model.findFriendsByName( name )
            if data is not None:
                self.view.showFriendTable( data )
            else:
                self.view.showMessage( "Error searching Friends" )
        else:
            self.view.showMessage( "Error in parameter name" )

    def addFriend( self ):
        friend = self.view.friendForm( None )
        if friend is not None:
            result = self.model.add( friend )
            if result > 0:
                self.view.showMessage( "Friend successfully added" )
            else:
                self.view.showMessage( "Friend has not been added" )
        else:
            self.view.showMessage( "Error in parameters" )

    def modifyFriend( self, oldVersion: Friend, newVersion: Friend ):
        result = self.model.modify( oldVersion, newVersion )
        if result > 0:
            self.view.showMessage( "Friend successfully modified" )
        else:
            self.view.showMessage( "Friend has not been modified" )
    
    def modifyFriendForm(self):
        phone = self.view.showInputDialog("Input phone: ")
        if phone is not None:
            friend = Friend(phone)
            oldFriend = self.model.find(friend)
            if oldFriend is not None:
                self.view.friendForm(oldFriend)
                self.view.showMessage("Input new data")
                newFriend = self.view.friendForm(None)
                if newFriend is not None:
                    result = self.model.modify(oldFriend, newFriend)
                    if int(result) > 0:
                        self.view.showMessage("Friend successfully modified")
                    else:
                        self.view.showMessage("Friend has not modified")
            else:
                self.view.showMessage("Friend not found")


    def removeFriend( self, friend: Friend ):
        result = self.model.remove( friend )
        if result > 0:
            self.view.showMessage( "Friend successfully removed" )
        else:
            self.view.showMessage( "Friend has not been removed" )


    def removeFriendForm( self ):
        phone = self.view.showInputDialog( "Input phone: " )
        if phone is not None:
            friend = Friend( phone )
            found = self.model.find( friend )
            if found is not None:
                self.removeFriend( friend )
            else:
                self.view.showMessage( "Friend not found" )
