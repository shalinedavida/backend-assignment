class Account:
    interest_rate = 0.05
    minimum_balance = 100
  
    def __init__(self,name):
        self.name=name
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        # self.transaction=[]
        self.loan_limit=400
        self.loan_amount=0
        self.frozen=False
        self.account_number=12345
        self.transactions=[]
        
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
        if amount > self.balance:
            return f"Insufficient funds .The transaction cannot go through"
        else:
            self.withdraw(amount)
            self.account_number.deposit(amount)
            return f"{amount} has been transferred successfully"

    # def transfer_funds(self,target_amount,amount):
    #     if amount <0:
    #         return"Invalid amount"
    #     if not instance (target_account,Account):
    #         return 'Target account must be an instance of a class' 
    #     if amount > self.get_balance:
    #         return "Insufficient balance"    
    #        self.withdraw(amount)            

    def get_balance(self):
        return sum(self.transaction) 

    # def request_loan(self,amount):
    #     if amount >self.loan_limit:
    #         return f"Your loan request has been denied"
    #     else:
    #         self.loan_amount += amount
    #         self.balance += amount  
    #         return f"Loan of {amount} approved .New balance is {self.balance}"
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

class Transaction:
    def __init__(self,date_and_time,narration,amount,transaction_type):
        self.date_and_time= date_and_time.now()
        self.narration=narration
        self.amount=amount
        self.transaction_type=transaction_type
        self._balance=0

    def deposits(self,amount):
        assert amount >0 ,"Amount must be positive"
        # transaction=Transaction()
        self._balance+=amount
        self.transactions.append(deposit)

    def withdraw(self,amount):
        assert amount > 0,"Amount must be positive"
        # transaction=Transaction()
        self._balance-=amount
        self.transactions.append(withdraw)

    def get_balance(self,transactions):
        for i, transaction in enumerate(transactions):
            print(f"Index {i}: {transaction}")   
       

