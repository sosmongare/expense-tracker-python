class ExpenseTracker:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    def add_expense(self, amount, description):
        self.balance -= amount
        self.transactions.append(f"Expense: ${amount} - {description}")

    def add_income(self, amount, description):
        self.balance += amount
        self.transactions.append(f"Income: ${amount} - {description}")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

    def display_transactions(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Display Balance")
        print("4. Display Transactions")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            amount = float(input("Enter the expense amount: $"))
            description = input("Enter a description for the expense: ")
            tracker.add_expense(amount, description)
        elif choice == '2':
            amount = float(input("Enter the income amount: $"))
            description = input("Enter a description for the income: ")
            tracker.add_income(amount, description)
        elif choice == '3':
            tracker.display_balance()
        elif choice == '4':
            tracker.display_transactions()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
