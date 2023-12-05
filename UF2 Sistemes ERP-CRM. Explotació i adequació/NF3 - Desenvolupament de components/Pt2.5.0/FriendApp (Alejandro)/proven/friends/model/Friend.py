
class Friend:
    def __init__(self, phone=None, name=None, age=None):
        self.phone = phone
        self.name = name
        self.age = age

    def getPhone(self):
        return self.phone
    
    def setPhone(self, phone):
        self.phone = phone
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        
    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age

    def __hash__(self):
        return super().__hash__()

    def __eq__(self, __o):
        return super().__eq__(__o)

    def __str__(self):
        return f"Friend{{phone={self.phone}, name={self.name}, age={self.age}}}"
