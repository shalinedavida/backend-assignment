class Account:
    interest_rate = 0.05
    minimum_balance = 100
    def __init__(self,name):
        self.name=name
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.transaction=[]
        self.loan_limit=400
        self.loan_amount=0
        self.frozen=False
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        self.deposits.append(amount)
        return f"Confirmed you have received {amount} new balance is {self.balance}"

    def withdraw(self,amount):
        if self.balance<0:
            return f"Insufficient funds"
        else:
            self.balance -= amount
            self.transaction.append(amount)
            return f"You have successfully withdrawn ! Your new balance {self.balance}"   

    def transfer_funds(self,amount):
        if amount>self.balance:
            return f"Insufficient funds .The transaction cannot go through"
        else:
            self.withdraw(amount)
            account_number.deposit(amount)
            return f"{amount} has been transferred successfully"

    def get_balance(self):
        return sum(self.transaction) 

    def request_loan(self,amount):
        if amount >self.loan_limit:
            return f"Your loan request has been denied"
        else:
            self.loan_amount += amount
            self.balance += amount  
            return f"Loan of {amount} approved .New balance is {self.balance}"  
        
    def repay_loan(self,amount):
        self.loan_amount -= amount
        self.balance -= amount
        return f"Loan repayment is successful"

    def view_account(self): 
        return f"Hello {self.name} your current account balance is {self.balance}"

    def change_owner(self,new_name):
        self.name=new_name
        return f"The new account owner is {self.name}"

    # def account_statement(self):
    #     for transaction in transactions:


    def interest(self):
       interest= self.balance * self.interest_rate
       self.balance += interest
       return f"This is the new amount {self.balance}"

    def freeze(self):
        self.frozen = True
        return f"This account is frozen"

    def unfreeze(self):
        self.frozen= False  
        return f" This account is now unfrozen" 

    def minimum_balance(self,amount):
        min_balance=self.balance - amount
        return min_balance >= self.minimum_balance

    def close_account(self):
        self.balance = 0
        self.transaction.clear()
        return f"Account cleared. All transactions removed."

