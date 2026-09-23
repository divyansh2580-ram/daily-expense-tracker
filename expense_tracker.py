# Daily Expense Tracker

def add_expense(expenses_list):
    amt_str = input("Enter amount: ")
    
    # Using simple if-else conditional instead of try-except
    if amt_str.isdigit() == True:
        amt = float(amt_str)
        date = input("Enter date (DD-MM-YYYY): ")
        cat = input("Enter category (Food, Travel, etc): ")
        
        # Tuple assignment and list operation
        record = (cat, amt, date)
        expenses_list.append(record)
        print("Expense added.")
        print()
    else:
        print("Wrong input. Put a number.")
        print()

def show_summary(expenses_list):
    if len(expenses_list) == 0:
        print("No expenses to show.")
        print()
    else:
        summary_dict = {} 
        
        # Iteration using a for loop
        for item in expenses_list:
            # Accessing tuple elements by index instead of advanced unpacking
            cat = item[0]
            amt = item[1]
            
            # Checking dictionary keys
            if cat in summary_dict:
                summary_dict[cat] = summary_dict[cat] + amt
            else:
                summary_dict[cat] = amt
                
        print("--- Summary ---")
        for key in summary_dict:
            # Basic print statement without f-strings
            print(key, ": Rs.", summary_dict[key])
        print("---------------")
        print()

def main():
    my_expenses = [] 
    
    run = True
    # Iteration statement (while)
    while run == True:
        print("1. Add Expense")
        print("2. Show Summary")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        # Conditional if-elif-else block
        if choice == "1":
            add_expense(my_expenses)
        elif choice == "2":
            show_summary(my_expenses)
        elif choice == "3":
            run = False
        else:
            print("Invalid choice")
            print()

# Standard function call
main()
    main()
