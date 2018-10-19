class BankAccount:
    acc_no = ''
    bal = 0

    def __init__(self, acc_no):
        self.acc_no = acc_no
        self.bal = 0

    def get_acc_no(self):
        return self.acc_no

    def get_bal(self):
        return self.bal

    def deposit(self, amt):
        self.bal += amt

    def withdraw(self, amt):
        if self.bal >= amt:
            self.bal -= amt
        else:
            print("You are too poor")

    def get_interest_rate(self):
        if str(self.acc_no).startswith('1'):
            return 0.01
        elif str(self.acc_no).startswith('0'):
            return 0.005

    def get_interest(self):
        return self.bal * self.get_interest_rate()


acc = BankAccount('00-12345-11')

acc.deposit(500)
print(f"You have", acc.bal)

acc.withdraw(100)
print(f"You are left with", acc.bal)

print(f"Your interest rate is", acc.get_interest_rate())
print(f"Your interest earned is", acc.get_interest())