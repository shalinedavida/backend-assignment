from datetime import datetime


class Transaction:
    def __init__(self,narration,amount,transaction_type):
        self.date_and_time= datetime.now()
        self.narration=narration
        self.amount=amount
        self.transaction_type=transaction_type
       
     def __str__(self):  
        return(f{self.date_and_time},{self.transaction_type},f"{self.amount},{self.narration}")

class Account:
    interest_rate = 0.05
    minimum_balance = 100
  
    def __init__(self,name):
        self.name=name
        self.deposits=[]
        self.withdrawals=[]
        self.loan_balance=0
        self.frozen=False
        self.account_number=account_number
        self.transactions=[]
        
    def deposit(self,amount):
        if amount < 0:
            return"Insufficient funds"
        self.deposits.append(amount)
        self.transactions.appemd(f"Deposit : {amount}")
        self.balance=self.get_balance()
        return f"Confirmed you have received {amount} new balance is {self.balance}"
    
    def withdraw(self,amount):
        if self.balance<0:
            return f"Insufficient funds"
        else:
          self.withdrawal.append(amount)
            self.transactions.append(f"Withdrawal: {amount}")
            self.balance=self.get_balance()
            return f"You have successfully withdrawn ! Your new balance {self.balance}"   


    def transfer_funds(self,target_account,amount):
        if amount <0:
            return"Invalid amount"
        if not instance (target_account,Account):
            return 'Target account must be an instance of a class' 
        if amount <= self.get_balance():    
           self.withdrawal(amount)
           target_account.deposit(amount) 
           account_balance=self.get_balance()  
           return f"{amount} has been transferred to {target_account.name}"         


    def get_balance(self,transactions):
        for i, transaction in enumerate(transactions):
            print(f"Index {i}: {transaction}")   
       

    
    def calculate_loan_limit(self):
        total_deposits = sum(self.deposits)
        return total_deposits//3

    def request_loan(self,amount):
        if is_frozen:
            return "Account is frozen.Cant request loan"  
        if amount > 0:
            self.loan_balance += amount
            self.deposit(amount)
            self.transactions.append(f"loan on ${amount} requested") 
            return f"loan of ${amount} approved" 
        else:
            return "Invalid request"             
        
    def repay_loan(self,amount):
        self.loan_amount -= amount
        self.balance -= amount
        return f"Loan repayment is successful"
              

    def view_account(self): 
        return f"Hello {self.name} your current account balance is {self.balance}"

    def change_owner(self,new_name):
        self.name=new_name
        return f"The new account owner is {self.name}"

    def account_statement(self):
       for i in self.deposits:
          print( f"Deposits{[i]}")
       
       for m in self.withdrawals:
          print(f"Withdrawals{[m]}")
 

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
        if amount >= 0:
            self.minimum_balance = amount
            return f"Minimum balance successfully set to {amount}"
        return f"Insufficient amount"

    def close_account(self):
        self.balance = 0
        self.transaction.clear()
        return f"Account cleared. All transactions removed."

   

