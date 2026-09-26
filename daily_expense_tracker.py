def add_expense(cat_list, amt_list, dt_list):
    print("\n-- Adding New Expense --")
    c = input("Category (e.g., Food, Travel, Books): ")
    a = input("Amount in Rs: ")
    
    # Checking if the user typed a valid number using basic string method
    if a.isdigit() == True:
        d = input("Date (DD-MM-YYYY): ")
        
        # Adding to our parallel lists
        cat_list.append(c)
        amt_list.append(int(a))
        dt_list.append(d)
        print("Expense added successfully!")
    else:
        print("Invalid amount. Please enter numbers only.")

def view_all(cat_list, amt_list, dt_list):
    print("\n-- All Expenses --")
    if len(cat_list) == 0:
        print("Nothing added yet.")
    else:
        # Basic iteration using range and len
        for i in range(len(cat_list)):
            print("Expense", i + 1)
            print("Category:", cat_list[i])
            print("Amount: Rs.", amt_list[i])
            print("Date:", dt_list[i])
            print("----------------")

def category_summary(cat_list, amt_list):
    print("\n-- Category Summary --")
    if len(cat_list) == 0:
        print("Nothing to show.")
    else:
        checked = []
        for i in range(len(cat_list)):
            current_cat = cat_list[i]
            
            # Check if we already calculated this category
            if current_cat not in checked:
                checked.append(current_cat)
                
                cat_total = 0
                for j in range(len(cat_list)):
                    if cat_list[j] == current_cat:
                        cat_total = cat_total + amt_list[j]
                        
                print(current_cat + ": Rs. " + str(cat_total))

def total_expense(amt_list):
    print("\n-- Total Expense --")
    total = 0
    for amt in amt_list:
        total = total + amt
    print("Total overall expense: Rs. " + str(total))

def main():
    # Local lists to hold the data
    category_list = []
    amount_list = []
    date_list = []
    
    # New Feature: Welcome and Name Input
    print("===================================")
    print("   Welcome to Expense Tracker")
    print("===================================")
    user_name = input("Please enter your name to start: ")
    print("\nHello, " + user_name + "! Let's manage your budget.")
    
    running = True
    while running == True:
        print("\n--- Main Menu ---")
        print("1. Add Expense")
        print("2. View All")
        print("3. Category Summary")
        print("4. Total Expense")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_expense(category_list, amount_list, date_list)
        elif choice == '2':
            view_all(category_list, amount_list, date_list)
        elif choice == '3':
            category_summary(category_list, amount_list)
        elif choice == '4':
            total_expense(amount_list)
        elif choice == '5':
            print("Goodbye, " + user_name + "!")
            running = False
        else:
            print("Invalid choice, please try again.")

# Starting the program
main()