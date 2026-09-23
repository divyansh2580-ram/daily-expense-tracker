# Expense Tracker for Grow Up Classes

def add_expense(record_list):
    amount_input = input("Enter amount spent: ")
    
    # checking if I typed a number
    if amount_input.isdigit() == True:
        money = float(amount_input)
        date = input("Enter date (DD-MM-YYYY): ")
        # using real things we buy for the institute and business
        category = input("Enter category (e.g., Pamphlets, Markers, Divyansh Sir salary, Vestige stock): ")
        
        entry = (category, money, date)
        record_list.append(entry)
        print("Done. Expense saved.")
        print()
    else:
        print("Error: Type a number without decimals.")
        print()

def show_summary(record_list):
    if len(record_list) == 0:
        print("Nothing to show yet.")
        print()
    else:
        totals = {} 
        
        # looping through the records
        for item in record_list:
            cat = item[0]
            money = item[1]
            
            # add to existing category or make a new one
            if cat in totals:
                totals[cat] = totals[cat] + money
            else:
                totals[cat] = money
                
        print("--- Total Spendings ---")
        for key in totals:
            print(key, ": Rs.", totals[key])
        print("-----------------------")
        print()

def main():
    my_ledger = [] 
    
    running = True
    while running == True:
        print("1. Add New Expense")
        print("2. See Total Spending")
        print("3. Close Program")
        
        choice = input("Pick an option: ")
        
        if choice == "1":
            add_expense(my_ledger)
        elif choice == "2":
            show_summary(my_ledger)
        elif choice == "3":
            running = False
        else:
            print("Wrong choice.")
            print()

# start program
main()