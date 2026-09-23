expenses = []


def add_expense():
    category = input("Enter expense category: ")
    amount_text = input("Enter amount in rupees: ")
    date = input("Enter date (DD-MM-YYYY): ")

    if category != "" and amount_text.isdigit() and date != "":
        amount = int(amount_text)
        expense = (category, amount, date)
        expenses.append(expense)
        print("Expense added successfully.")
    else:
        print("Invalid input. Category, amount, and date cannot be empty.")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses added yet.")
    else:
        print("\n--- All Expenses ---")
        index = 0

        while index < len(expenses):
            print("Category:", expenses[index][0])
            print("Amount: Rs.", expenses[index][1])
            print("Date:", expenses[index][2])
            print("-------------------")
            index = index + 1


def show_summary():
    category_total = {}

    if len(expenses) == 0:
        print("No expenses available for summary.")
    else:
        index = 0

        while index < len(expenses):
            category = expenses[index][0]
            amount = expenses[index][1]

            if category in category_total:
                category_total[category] = category_total[category] + amount
            else:
                category_total[category] = amount

            index = index + 1

        print("\n--- Category-wise Expense Summary ---")

        for category in category_total:
            print(category, ": Rs.", category_total[category])


def show_total_expense():
    total = 0
    index = 0

    while index < len(expenses):
        total = total + expenses[index][1]
        index = index + 1

    print("Total expense: Rs.", total)


choice = "0"

while choice != "5":
    print("\n===== DAILY EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Category-wise Summary")
    print("4. View Total Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        show_total_expense()
    elif choice == "5":
        print("Thank you for using Daily Expense Tracker.")
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")")

if __name__ == "__main__":
    main()
