class Category:  # Categories in a monthly budget

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def check_balance(self):
        print("Current balance is %d" % self.amount)
        if self.amount < 100:
            print("Funds are a bit low. Consider a transfer, deposit, or just spending less")
        return self.amount

    def deposit(self, deposit_amt):
        self.amount = self.amount + deposit_amt
        print("%d has been deposited" % deposit_amt)
        return self.amount, deposit_amt

    def withdraw(self, withdraw_amt):
        if self.amount >= withdraw_amt:  # You cannot have a budget of less than 0
            self.amount = self.amount - withdraw_amt
            print("%d has been withdrawn from %s" % (withdraw_amt, self.name))
            return self.amount, withdraw_amt
        else:
            print("Not enough funds in budget!")

    def transfer(self, self2, amt):  # Enter category you will transfer to and amount
        if self.amount >= amt:
            self.amount = self.amount - amt
            self2.amount = self2.amount + amt
            print("%d transferred to %s from %s" % (amt, self.name, self2.name))
            return self.amount, self2.amount
        else:
            print("Not enough funds in %s category to transfer!" % self.name)


category_1 = Category('Food', 200)  # Includes groceries and dining out
category_2 = Category('Clothing', 100)
category_3 = Category('Hair', 100)  # Bi-weekly salon visit
category_4 = Category('Car', 300)  # Includes car note and gas
category_5 = Category('Entertainment', 20)
category_6 = Category('Toiletries', 100)  # Includes shampoo, soap, etc.



