class BankAccount:
    def __init__(self):
        self.__balance = 1000
    def show_balance(self):
        print("Balance",self.__balance)    
    def deposit(self,amount):
        self.__balance += amount
        print("Money Added !")    

account = BankAccount()
account.show_balance()
account.deposit(500)
account.show_balance()