# 4. Class Variables and Class Methods
#Assignment:
#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "UBL Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Bank Name: {self.bank_name}")

# Creating instances
account1 = Bank("Alice")
account2 = Bank("Bob")

# Displaying information before changing the bank name
account1.display_info()
account2.display_info()

# Changing the bank name
Bank.change_bank_name("HBL Bank")

# Displaying information after changing the bank name
account1.display_info()
account2.display_info()
