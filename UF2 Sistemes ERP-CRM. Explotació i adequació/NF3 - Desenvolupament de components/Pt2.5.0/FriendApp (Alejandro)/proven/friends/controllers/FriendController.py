import sys

from proven.friends.views.FriendView import FriendView
from proven.friends.model.Friend import Friend
from proven.friends.model.FriendModel import FriendModel

"""
FriendController.py
Class FriendController. Friend controller. Uses the
FriendModel class. Uses the FriendView class.
Author: ProvenSoft
Version: 1.0
"""


class FriendController:

    def __init__(self, model: FriendModel):
        self.model = model
        self.view = FriendView(self, model)
        self.view.display()

    def processRequest(self, action):
        if action is None:
            action = "wrong_action"
        if action == "exit":
            self.exit_application()
        elif action == "list_all_friends":
            self.listAllFriends()
        elif action == "search_friend_by_phone":
            self.searchFriendByPhone()
        elif action == "friend_form_remove":
            self.removeFriend()
        elif action == "friend_form_add":
            self.addFriend()
        elif action == "search_friends_by_name":
            self.searchFriendByName()
        elif action == "friend_form_modify":
            self.modifyFriendForm()
        elif action == "wrong_action":
            self.view.showMessage("Wrong option")
    
    def exit_application(self):
        sys.exit(0)

    def listAllFriends(self):
        data = self.model.findAll()
        if data is not None:
            self.view.showFriendTable(data)
        else:
            self.view.showMessage("Error retrieving data")

    def searchFriendByPhone(self):
        while True:
            phone = self.view.shoInputDialog("Input phone: ")
            if self.view.phoneForm(phone) is not False:
                break
        if phone is not None:
            friend = Friend(phone)
            found = self.model.find(friend)
            if found is not None:
                self.view.friendForm(found)
            else:
                self.view.showMessage("Friend not found")
        else:
            self.view.showMessage("Error in parameter phone")

    def searchFriendByName(self):
        while True:
            name = self.view.shoInputDialog("Input name: ")
            if self.view.nameForm(name) is not False:
                break
        if name is not None:
            data = self.model.findFriendsByName(name)
            if data is not None:
                self.view.showFriendTable(data)
            else:
                self.view.showMessage("Error searching Friends")
        else:
            self.view.showMessage("Error in parameter name")

    def addFriend(self):
        friend = self.view.friendForm(None)
        if friend is not None:
            result = self.model.add(friend)
            if int(result) > 0:
                self.view.showMessage("Friend successfully added")
            else:
                self.view.showMessage("Friend has not added")
        else:
            self.view.showMessage("Error in parameters")

    def modifyFriend(self, old_version, new_version):
        result = self.model.modify(old_version, new_version)
        if result > 0:
            self.view.showMessage("Friend successfully modified")
        else:
            self.view.showMessage("Friend has not modified")

    def modifyFriendForm(self):
        while True:
            phone = self.view.shoInputDialog("Input phone: ")
            if self.view.phoneForm(phone) is not False:
                break
        if phone is not None:
            friend = Friend(phone)
            found = self.model.find(friend)
            if found is not None:
                self.view.friendForm(found)
                self.view.showMessage("Input new data")
                new_friend = self.view.friendForm(None)
                if new_friend is not None:
                    result = self.model.modify(found, new_friend)
                    if int(result) > 0:
                        self.view.showMessage("Friend successfully modified")
                    else:
                        self.view.showMessage("Friend has not modified")
            else:
                self.view.showMessage("Friend not found")

    def removeFriend(self):
        while True:
            phone = self.view.shoInputDialog("Input phone: ")
            if self.view.phoneForm(phone) is not False:
                break
        if phone is not None:
            friend = Friend(phone)
            found = self.model.find(friend)
            if found is not None:
                self.view.friendForm(found)
                result = self.model.remove(found)
                if int(result) > 0:
                    self.view.showMessage("Friend successfully removed")
                else:
                    self.view.showMessage("Friend has not removed")
            else:
                self.view.showMessage("Friend not found")
