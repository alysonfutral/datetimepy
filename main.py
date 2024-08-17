from datetime import datetime

lst = []
while (1): # Infinite loop to print the menu again and again till quit option is not choosen
    print("Main Menu : ")
    print("1. List all incomplete todo items")
    print("2. List incomplete todo items due today")
    print("3. Add a todo item")
    print("4. Complete a todo item")
    print("5. Quit")
  
    choice = int(input("Enter your choice > "))
  
    if choice == 1:
        print("\nIncomplete items:")
        for tpl in lst:
            print(f"\t{tpl[0]} due {str(tpl[1])}")
          
    elif choice == 2:
        print("\nIncomplete items due today:")
        CurrentDate = datetime.now()
        for tpl in lst:
            if tpl[1].date() == CurrentDate.date():
                print(f"\t{tpl[0]} due {str(tpl[1])}")
              
    elif choice == 3:
        desc = input("\nEnter item description : ")
        duedate = input("Enter due date/time (MM/DD/YYYY hh:mm) : ")
        format = "%m/%d/%Y %H:%M"
        duedate = datetime.strptime(duedate, format)
        tpl = (desc, duedate)
        print(tpl)
        lst.append(tpl)


  
    elif choice == 4:
        if len(lst) != 0:
            print("\nIncomplete items:")
            x = 0
            for tpl in lst:
                print(f"\t{x}) {tpl[0]} due {str(tpl[1])}")
                x += 1
            delete = int(input("\nEnter item to complete : "))
            del lst[delete]
        else:
            print("No incomplete todo items available.")
          
    elif choice == 5:
        print("Bye!")
        exit()
    else:
        print("\n")