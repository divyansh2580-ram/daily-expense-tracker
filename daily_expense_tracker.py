# Lists to hold the data
category_list = []
amount_list = []
date_list = []

# Starting Header and Name Input
print("===================================")
print("       Expense Tracker             ")
print("===================================")
user = input("What's your name? ")
print("\nHey " + user + ", let's manage your budget.")

# Main Program Loop
while True:
    print("\n--- Daily Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All")
    print("3. Category Summary")
    print("4. Total Expense")
    print("5. Exit")
    
    opt = input("Type your choice (1 to 5): ")
    
    if opt == '1':
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
            
    elif opt == '2':
        total_items = len(category_list)
        if total_items == 0:
            print("No expenses recorded yet.")
        else:
            for idx in range(total_items):
                print("\nExpense No.", idx + 1)
                print("Category:", category_list[idx])
                print("Amount:", amount_list[idx], "Rs")
                print("Date:", date_list[idx])
                
    elif opt == '3':
        total_items = len(category_list)
        if total_items == 0:
            print("List is empty.")
        else:
            visited = []
            for x in range(total_items):
                cat = category_list[x]
                
                if cat not in visited:
                    visited.append(cat)
                    
                    s = 0
                    for y in range(total_items):
                        if category_list[y] == cat:
                            s = s + amount_list[y]
                            
                    print(cat + " -> Rs.", s)
                    
    elif opt == '4':
        final_total = sum(amount_list)
        print("Your total expenses are: Rs.", final_total)
        
    elif opt == '5':
        print("Catch you later, " + user + "!")
        break
        
    else:
        print("Incorrect choice. Press 1, 2, 3, 4, or 5.")