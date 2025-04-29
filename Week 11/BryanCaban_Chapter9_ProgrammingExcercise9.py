# Programing Exercise 9: Bank Account Class
# Author: Bryan Caban
# Date: 27/03/2022
# BankAcct Class: Represents a bank account with attributes for name, account number, balance, and interest rate.  
# Methods include adjusting interest rate, depositing, withdrawing, retrieving balance, calculating interest,  
# and displaying account details. A test function verifies all functionalities.  


class BankAcct:
    def __init__(self, name, account_number, amount=0.0, interest_rate=0.01):
        """Initialize a bank account with the given parameters.
        
        Args:
            name (str): Account holder's name
            account_number (str): Unique account number
            amount (float, optional): Initial deposit amount. Defaults to 0.0.
            interest_rate (float, optional): Annual interest rate (decimal). Defaults to 0.01 (1%).
        """
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate
    
    def adjust_interest_rate(self, new_rate):
        """Adjust the account's interest rate.
        
        Args:
            new_rate (float): New annual interest rate (decimal)
        """
        self.interest_rate = new_rate
        return self.interest_rate
    
    def withdraw(self, amount):
        """Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            float: New balance after withdrawal
            
        Raises:
            ValueError: If withdrawal amount exceeds balance
        """
        if amount > self.amount:
            raise ValueError("Insufficient funds")
        
        self.amount -= amount
        return self.amount
    
    def deposit(self, amount):
        """Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            float: New balance after deposit
        """
        self.amount += amount
        return self.amount
    
    def get_balance(self):
        """Get the current account balance.
        
        Returns:
            float: Current balance
        """
        return self.amount
    
    def calculate_interest(self, days):
        """Calculate interest for the specified number of days.
        
        Args:
            days (int): Number of days to calculate interest for
            
        Returns:
            float: Interest amount earned
        """
        # Calculate daily interest rate (annual rate / 365)
        daily_rate = self.interest_rate / 365
        
        # Calculate interest amount
        interest_amount = self.amount * daily_rate * days
        
        return interest_amount
    
    def __str__(self):
        """Return a string representation of the account.
        
        Returns:
            str: Formatted account information
        """
        return f"Account: {self.account_number}\nHolder: {self.name}\nBalance: ${self.amount:.2f}\nInterest Rate: {self.interest_rate:.2%}"


def test_bank_account():
    """Test function to validate BankAcct class functionality."""
    print("Creating a new bank account...")
    account = BankAcct("John Doe", "12345678", 1000.0, 0.05)
    print(account)
    print()
    
    print("Testing deposit method...")
    account.deposit(500.0)
    print(f"New balance after $500 deposit: ${account.get_balance():.2f}")
    print()
    
    print("Testing withdrawal method...")
    try:
        account.withdraw(200.0)
        print(f"New balance after $200 withdrawal: ${account.get_balance():.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    print()
    
    print("Testing interest rate adjustment...")
    new_rate = 0.06  # 6%
    account.adjust_interest_rate(new_rate)
    print(f"New interest rate: {account.interest_rate:.2%}")
    print()
    
    print("Testing interest calculation...")
    days = 30
    interest = account.calculate_interest(days)
    print(f"Interest earned over {days} days: ${interest:.2f}")
    print()
    
    print("Testing insufficient funds scenario...")
    try:
        account.withdraw(2000.0)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    
    print("Final account status:")
    print(account)


if __name__ == "__main__":
    test_bank_account()