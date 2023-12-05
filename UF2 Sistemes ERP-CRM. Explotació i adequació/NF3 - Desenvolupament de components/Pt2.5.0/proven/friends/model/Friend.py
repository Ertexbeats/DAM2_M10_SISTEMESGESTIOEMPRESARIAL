class Friend:
    # def __init__( self, *args ):
    #     if self( args ) == None:
    #         self.phone
    #         self.name
    #         self.age
    #     elif len( args ) == 1:
    #         self.phone == args[ 0 ]
    #         self.name
    #         self.age
    #     else:
    #         self.phone = args[ 0 ]
    #         self.name = args[ 1 ]
    #         self.age = args[ 2 ]

    def __init__( self, phone = "", name = "", age = 0 ):
        self.phone = phone
        self.name = name
        self.age = age

    # GETTER & SETTERS
    def getPhone( self ):
        return self.phone

    def setPhone( self, phone ):
        self.phone = phone

    def getName( self ):
        return self.name

    def setName( self, name ):
        self.name = name

    def getAge( self ):
        return self.age

    def setAge( self, age ):
        self.age = age

    def __eq__( self, other ):
        if isinstance( other, Friend ):
            return self.phone == other.phone
        return False

    # TOSTRING
    def __str__( self ):
        return (f"Friend: "
                f"phone: {self.phone}, "
                f"name: {self.name}, "
                f"age: {self.age}")


# TESTS
# friend1 = Friend( "651111176", "Miguel", 20 )
# phone = friend1.getPhone()
# print( "getPhone: ", phone )
# name = friend1.getName()
# print( "getName: ", name )
# age = friend1.getAge()
# print( "getAge: ", age )
# print( "friend1: ", friend1 )
#
# friend2 = Friend()
# phone2 = "651111177"
# friend2.setPhone( phone2 )
# name2 = "Pepe"
# friend2.setName( name2 )
# age2 = 88
# friend2.setAge( age2 )
# print( "friend2: ", friend2 )
