category_list = []
amount_list = []
date_list = []

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
        d = input("Date: ")
        
        category_list.append(c)
        amount_list.append(int(a))
        date_list.append(d)
        
        print("Expense added!")
        
    elif choice == '2':
        if len(category_list) == 0:
            print("Nothing added yet.")
        else:
            for i in range(len(category_list)):
                print("\nExpense", i + 1)
                print("Category:", category_list[i])
                print("Amount: Rs.", amount_list[i])
                print("Date:", date_list[i])
                
    elif choice == '3':
        if len(category_list) == 0:
            print("Nothing to show.")
        else:
            # Beginner way to find unique categories without using dictionaries
            checked = []
            for i in range(len(category_list)):
                current_cat = category_list[i]
                
                if current_cat not in checked:
                    checked.append(current_cat)
                    
                    # Find total for this specific category
                    cat_total = 0
                    for j in range(len(category_list)):
                        if category_list[j] == current_cat:
                            cat_total = cat_total + amount_list[j]
                            
                    print(current_cat + ": Rs. " + str(cat_total))
                    
    elif choice == '4':
        total = 0
        for amt in amount_list:
            total = total + amt
        print("Total expense: Rs. " + str(total))
        
    elif choice == '5':
        print("Bye!")
        break
        
    else:
        print("Invalid choice!")
