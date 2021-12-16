"""
Author: Anastasia Yazvinskaya, (Faud Torres), Lindsay Gardels, Christian Maciel
Class: CS 241 - 03 (Fall 2021)
Assignment: Team W04
"""

""" CORE REQUIREMENTS """
"""
1. Create a CheckingAccount class as defined above. It should be initialized to an initial balance and a number of checks as passed in to the __init__() function.

    The deposit method should increase the balance by the amount passed in. The write_check method should decrease the balance by the amount given and decrease the number of checks by 1.

    The display method should display the current balance and the number of checks.

    The apply_for_credit method can be left blank (i.e., "pass").

    Run the program, try each method, and verify that they work as expected.
"""
class CheckingAccount:
    def __init__(self,balance=0, num_of_checks=0):
        # 2
        if balance < 0:
            raise BalanceError("The balance can not be negative")
        
        self.balance = balance
        self.num_of_checks = num_of_checks

    def deposit(self, deposit=0):
        self.balance += deposit

    def write_check(self, check=0):
        # 2
        if self.balance-check < 0:
            raise BalanceError("The balance can not be negative")
        if self.num_of_checks-check < 0:
            raise BalanceError("The number of checks can not be negative")
        
        self.balance -= check
        self.num_of_checks -= 1

    def display(self):
        print(f"""Balance: {self.balance}
Number of checks: {self.num_of_checks}""")

    def apply_for_credit(self):
        pass
"""
2. Create classes for the exceptions BalanceError and OutOfChecksError. They should each inherit from the Exception class, and should accept a message as a parameter to the __init__ function. This message should then be passed to the __init__ function of the super class.

    Add logic to the CheckingAccount __init__ function and to the write_check function to raise an appropriate BalanceError if the resulting balance would be negative.

    Also, add logic to the CheckingAccount write_check function to raise an OutOfChecksError if there are no more checks.

    Test your code to ensure that the exceptions are raised as expected.
"""
class BalanceError(Exception):
    def __init__(self, message=""):
        super().__init__(message)
        """
        Stretch challenges
        3. Add an overage amount as a member variable to the BalanceError class. Then, set this amount whenever a BalanceError is raised. When handling the error, inform the use of how far over the balance they would have gone.
        """
        self.overage_amount = 0

class OutOfChecksError(Exception):
    def __init__(self, message=""):
        super().__init__(message)

""" STRETCH CHALLENGES """
"""
1. Raise a ValueError in deposit and write_check if the amount is negative. Raise a NotImplementedError in the apply_for_credit. Make sure to provide appropriate messages. Then, handle them in main. Verify that they work correctly.
"""
class CheckingAccountStretch:
    def __init__(self,balance=0, num_of_checks=0):
        if balance < 0:
            raise BalanceError("The balance can not be negative")
        
        self.balance = balance
        self.num_of_checks = num_of_checks
    
    """
    2. Change balance to a property (think getter / setter) and make sure exceptions are appropriately raised if an attempt is made to set the balance to a negative number.
    """
    @property
    def balance(self):
        return self.balance
    @balance.setter
    def balance(self, newBalance):
        if newBalance < 0:
            raise BalanceError("The balance can not be negative")
        self.balance = newBalance

    def deposit(self, deposit=0):
        if deposit < 0:
            raise ValueError
        self.balance += deposit

    def write_check(self, check=0):
        if check < 0:
            raise ValueError
        if self.balance-check < 0:
            raise BalanceError("The balance can not be negative")
        if self.num_of_checks-check < 0:
            raise BalanceError("The number of checks can not be negative")
        
        self.balance -= check
        self.num_of_checks -= 1

    def display(self):
        print(f"""Balance: {self.balance}
Number of checks: {self.num_of_checks}""")

    def apply_for_credit(self, amount):
        raise NotImplementedError

# Core Requirements
#print("CORE REQUIREMENTS")
#print()
# Stretch Challenges
#print("STRETCH CHALLENGES")
    

def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Desposit money")
    print("  check - Write a check")


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "quit":
        display_menu()
        command = input("Enter a command: ")
        """
        3. Handle the exceptions you raised above in main so that the program does not crash. If an BalanceError is caught, display the message. If an OutOfChecks error is caught. Ask the user if they would like to buy more checks. If so, add 25 checks and deduct $5.00 from the balance.

            Verify that the these exceptions are properly handled.
        """
        # Core Requirements
        print("CORE REQUIREMENTS")
        if command == "new":
            # 3
            try:
                balance = float(input("Starting balance: "))
                num_checks = int(input("Numbers of checks: "))

                acc = CheckingAccount(balance, num_checks)
            except BalanceError as err:
                print(f"Error: {err}")
        elif command == "display":
            acc.display()
        elif command == "deposit":
            amount = float(input("Amount: "))
            acc.deposit(amount)
        elif command == "check":
            # 3
            try:
                amount = float(input("Amount: "))
                acc.write_check(amount)
            except BalanceError as err:
                print(f"Error: {err}")
            except OutOfChecksError as err:
                print(f"Error: {err}")
                
                more_checks = input("Would you like to buy more checks (yes/no)? ")
                if more_checks == "yes":
                    acc.balance -= 5
                    acc.check_count += 25

        elif command == "credit":
            amount = float(input("Amount: "))
            acc.apply_for_credit(amount)

        # Stretch Challenges
        print("STRETCH CHALLENGES")
        if command == "new":
            try:
                balance = float(input("Starting balance: "))
                num_checks = int(input("Numbers of checks: "))

                acc = CheckingAccountStretch(balance, num_checks)
            except BalanceError as err:
                print(f"Error: {err}")
        elif command == "display":
            acc.display()
        elif command == "deposit":
            amount = float(input("Amount: "))
            acc.deposit(amount)
        elif command == "check":
            try:
                amount = float(input("Amount: "))
                acc.write_check(amount)
            except BalanceError as err:
                print(f"Error: {err}")
            except OutOfChecksError as err:
                print(f"Error: {err}")
                
                more_checks = input("Would you like to buy more checks (yes/no)? ")
                if more_checks == "yes":
                    acc.balance -= 5
                    acc.check_count += 25

        elif command == "credit":
            try:
                amount = float(input("Amount: "))
                acc.apply_for_credit(amount)
            except NotImplementedError as err:
                print(f"Error: {err}")


if __name__ == "__main__":
    main()