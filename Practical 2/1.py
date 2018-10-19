class Customer:
    __customer_id = ''
    __name = ''

    def __init__(self, id, name):
        if len(id) != 5:
            print("ID has incorrect length")
        elif id[-1].isalpha():
            print("Last digit is not alpha")
        else:
            self.__customer_id = id
            self.__name = name

    # Accessors
    def getID(self):
        return self.__customer_id

    def getName(self):
        return self.__name

    # Mutators
    def setID(self, id):
        self.__customer_id = id

    def setName(self, name):
        self.__name = name

c1 = Customer('1', 'Andy Tan')
print("===================")
print(f"Cust ID: {c1.getID()}")
print(f"Cust Name: {c1.getName()}")
c1.setID(2)
c1.setName('Chi Koon')
print("===================")
print(f"Cust ID: {c1.getID()}")
print(f"Cust Name: {c1.getName()}")