class BankAccount:
    __acc_no = ''
    __bal = 0

    def __init__(self, acc_no):
        self.__acc_no = acc_no
        self.__bal = 0

    def get_acc_no(self):
        return self.__acc_no

    def get_bal(self):
        return self.__bal

    def deposit(self, amt):
        self.__bal += amt

    def withdraw(self, amt):
        if self.__bal >= amt:
            self.__bal -= amt
        else:
            print("You are too poor")

    def get_interest_rate(self):
        if str(self.__acc_no).startswith('1'):
            return 0.01
        elif str(self.__acc_no).startswith('0'):
            return 0.005
        else:
            return 0

    def get_interest(self):
        return self.__bal * self.get_interest_rate()


acc = BankAccount('10-12345-11')

acc.deposit(500)
print(f"You have", acc.get_bal())

acc.withdraw(100)
print(f"You are left with", acc.get_bal())

print(f"Your interest rate is", acc.get_interest_rate())
print(f"Your interest earned is", acc.get_interest())