def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (e.g., Food, Transport, Utilities): ")
        
        # Store as a tuple (category, amount, date) and append to the list
        expenses.append((category, amount, date))
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid amount. Please enter a numerical value.\n")

def generate_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    
    summary = {}
    # Loop through the list of tuples
    for category, amount, date in expenses:
        # Populate the dictionary with category-wise totals
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
            
    print("\n--- Category-wise Expense Summary ---")
    for cat, total in summary.items():
        print(f"{cat}: ₹{total:.2f}")
    print("-------------------------------------\n")

def main():
    expenses = [] # List to store expense tuples
    
    while True:
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            generate_summary(expenses)
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()