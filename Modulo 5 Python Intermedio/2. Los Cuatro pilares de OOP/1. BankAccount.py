class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if  amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        BankAccount.__init__(self, balance)

        if min_balance < 0:
            raise ValueError("Minimum balance cannot be negative.")
        self.min_balance = min_balance


    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < self.min_balance:
            raise ValueError(f"cannot withdraw ${amount}. Minimum balance of ${self.min_balance} must be maintained.")
        
        BankAccount.withdraw(self, amount)

try:
    account = SavingsAccount(100, 20)
    print(f'Initial balance: ${account.balance} and minimum balance: ${account.min_balance}')

    account.deposit(50)
    print(f'Balance after deposit: ${account.balance}')

    account.withdraw(150)
    print(f'Balance after withdrawal: ${account.balance}')

except ValueError as e:
    print(e)


