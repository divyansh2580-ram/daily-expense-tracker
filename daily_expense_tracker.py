# Lists to hold the data
category_list = []
amount_list = []
date_list = []

# Starting Header and Name Input
print("===================================")
print("       Expense Tracker             ")
print("===================================")
name = input("Please enter your name to start: ")
print(f"\nHello {name}! Let's manage your budget.")

# Main Program Loop
while True:
    print("\n--- Daily Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All")
    print("3. Category Summary")
    print("4. Total Expense")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        c = input("Category: ")
        a = input("Amount in Rs: ")
        
        if a.isdigit():
            d = input("Date: ")
            category_list.append(c)
            amount_list.append(int(a))
            date_list.append(d)
            print("Expense added!")
        else:
            print("Invalid amount! Please enter numbers only.")
            
    elif choice == '2':
        if len(category_list) == 0:
            print("Nothing added yet.")
        else:
            for i in range(len(category_list)):
                print(f"\nExpense {i + 1}")
                print(f"Category: {category_list[i]}")
                print(f"Amount: Rs. {amount_list[i]}")
                print(f"Date: {date_list[i]}")
                
    elif choice == '3':
        if len(category_list) == 0:
            print("Nothing to show.")
        else:
            checked = []
            for i in range(len(category_list)):
                current_cat = category_list[i]
                
                if current_cat not in checked:
                    checked.append(current_cat)
                    
                    cat_total = 0
                    for j in range(len(category_list)):
                        if category_list[j] == current_cat:
                            cat_total += amount_list[j]
                            
                    print(f"{current_cat}: Rs. {cat_total}")
                    
    elif choice == '4':
        total = sum(amount_list)
        print(f"Total overall expense: Rs. {total}")
        
    elif choice == '5':
        print(f"Bye {name}!")
        break
        
    else:
        print("Invalid choice, please try again.")
