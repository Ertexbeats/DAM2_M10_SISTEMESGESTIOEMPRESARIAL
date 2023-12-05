from proven.friends.model.Friend import Friend

class FriendModel:
    def __init__( self ):
        self.friends = [ ]

    def find( self, entity ):
        if entity is not None:
            find_friend = self.findAll()
            for friend in find_friend:
                if friend.phone == entity.phone:
                    return friend
        else:
            return None

    def add( self, entity ):
        if entity is not None:
            self.friends.append( entity )
            return 1
        else:
            return 0

    def modify(self, old_entity, new_entity):
        if old_entity is not None and new_entity is not None:
            if (old_entity.phone == new_entity.phone and old_entity.name == new_entity.name and old_entity.age == new_entity.age):
                return 0
            else:
                self.friends.remove(old_entity)
                self.friends.append(new_entity)
                return 1
        else:
            return 0

    def remove( self, entity ):
        if entity is not None:
            self.friends.remove( entity )
            return 1
        else:
            return 0

    def findAll( self ):
        return self.friends

    def findFriendsByName( self, name ):
        friends = None
        if name is not None:
            all_friends = self.findAll()
            friends = []
            for friend in all_friends:
                if friend.name.lower() == name.lower():
                    friends.append(Friend(friend.name, friend.phone, friend.age))
        return friends

    def __str__( self ):
        return f"Friends: {self.friends}"
