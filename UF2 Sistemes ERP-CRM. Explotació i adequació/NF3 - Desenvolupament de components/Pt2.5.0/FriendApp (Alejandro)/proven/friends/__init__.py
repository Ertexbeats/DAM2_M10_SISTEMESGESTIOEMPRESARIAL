from proven.friends.model.FriendModel import FriendModel
from proven.friends.controllers.FriendController import FriendController
"""
FriendsApp.py
Application to manage friends and categories.
Uses the FriendController class.
Author: ProvenSoft
Version: 1.0"""

class FriendApp:
    def run(self):
        FriendController(FriendModel())

main = FriendApp()
main.run()