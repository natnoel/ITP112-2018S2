class Customer:
    __customer_id = ''
    __name = ''

    def __init__(self, id, name):
        if self.is_valid_id(id):
            self.__customer_id = id
        self.__name = name

    # Accessors
    def get_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    # Mutators
    def set_id(self, id):
        if self.is_valid_id(id):
            self.__customer_id = id

    def set_name(self, name):
        self.__name = name

    @staticmethod
    def is_valid_id(id):
        if len(id) != 5:
            print("ID has incorrect length")
            return False
        elif not id[-1].isalpha():
            print("Last digit is not alpha")
            return False
        else:
            return True


c1 = Customer('12345', 'Andy Tan')
print("===================")
print(f"Cust ID: {c1.get_id()}")
print(f"Cust Name: {c1.get_name()}")
c1.set_id('2')
c1.set_name('Chi Koon')
print("===================")
print(f"Cust ID: {c1.get_id()}")
print(f"Cust Name: {c1.get_name()}")
c1.set_id('2758d')
c1.set_name('Mr Lee')
print("===================")
print(f"Cust ID: {c1.get_id()}")
print(f"Cust Name: {c1.get_name()}")