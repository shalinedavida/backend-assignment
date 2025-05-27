class Account:
    def __init__(self,name):
        self.name=name
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.transaction=[]
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        self.deposits.append(amount)
         return f"Confirmed you have received {amount} new balance is {self.balance}"

    def withdraw(self,amount,balance):
        if self.balance<0:
            return f"Insufficient funds"
        else:
            self.balance-= amount
            self.transaction.append(amount)
            return f"You have successfully withdrawn ! Yournew balance {self.balance}"   

    def transfer_funds(self,amount,account_number):
        if amount>self.balance:
            return f"Insufficient funds .The transaction cannot go through"
        else:
            self.withdraw(amount)
            account_number.deposit(amount)
            return f"{amount} has been transferred successfully"
    def get_balance(self):
        return sum(self.transaction) 
    def request_loan(self):
        
    def repay_loan(self):
    def view_account(self):           
    def change_owner(self):
    def account_statement(self):
    def interest(self):
    def freeze(self):
    def minimum_balance(self):
    def close_account(self):

