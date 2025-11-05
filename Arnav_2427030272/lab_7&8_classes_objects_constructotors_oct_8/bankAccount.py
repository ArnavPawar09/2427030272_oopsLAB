"""
- create a py class clled bankAccount which represents a bank acc having as attributes :
  acc no, name, balance
- create a constructor with parameters :
  acc no, name, balance
- create a deposit method which manages deposit actions
- create a withdrawl method which manages withdrawl actions
- create a bankFees method to apply bank fees with 5% of the balance
- create a display method to display acc details
"""

class bankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawl(self, amount):
        self.balance -= amount

    def bankFees(self):
        bank_fees = self.balance*0.05
        print(bank_fees,"\n")

    def display(self):
        print("account no :", self.acc_no)
        print("balance :", self.balance)
        print("bank fees :", end=" ")
        self.bankFees()

MyAcc = bankAccount(12345, "Arnav", 1000)
MyAcc.display()
MyAcc.deposit(1000)
MyAcc.display()
MyAcc.withdrawl(500)
MyAcc.display()
