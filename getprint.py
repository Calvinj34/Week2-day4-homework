class Cart():

    def __init__(self, name, day, store,item):
        self.name = name
        self.store = store
        self.day = day
        self.item = item

    def addtocart(self,item,):
        self.item = item
        
       

    def inthecart(self):
        string = f'Hi my name is {self.name}, it is {self.day} and I am at {self.store}, This is whats in my cart {self.item}'
        print(string.upper())
        return(string)

c1 = Cart('John', 'wednesday','kingsoopers','candy' )

c1.inthecart()