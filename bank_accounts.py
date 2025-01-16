#to open a bank account 🏦



class BankAccount: 
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

  #here str means string as the contactenanation is done with string
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.account_id} {self.account_type} {self.pin} {self.balance}"
    
    def deposit(self,amount):
       self.balance = self.balance + amount
       return self.balance


    def withdraw(self,amount):
        self.balance = self.balance - amount
        return self.balance
      

    def display_balance(self):
       print(f"{self.balance}rs")



visitor = BankAccount("John", "Doe", 123456, "Savings", 1234, 000)

visitor.deposit(96)
visitor.display_balance() 
visitor.withdraw(25)
visitor.display_balance() 
print(visitor)












