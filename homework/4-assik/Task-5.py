class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance   # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print("Deposit successful")
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive")
        else:
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("Withdrawal successful")
            else:
                print("Not enough balance")

    def get_balance(self):
        return self.__balance




owner = input("Enter owner name: ")
balance = int(input("Enter initial balance: "))

account = BankAccount(owner, balance)

choice = 0
while choice != 4:
    print()
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Show balance")
    print("4 - Exit")

    choice = int(input("Choose option: "))

    if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 3:
        print("Balance:", account.get_balance())

    elif choice == 4:
        print("Goodbye")

    else:
        print("Invalid option")
