print("WELCOME TO HELLO BAR!!!")
name=input("Whats your name?:").title()
print(f"Hello {name}")
try:
    age=int(input(f"Whats your age, {name}\n"))
except ValueError:
    print("Invalid Age!")
    quit()

if age < 18:
        print("You are not allowed!")
else:
        print("You can go inside!")
        while True:
            print("MENU\n1.Coke\n2.Juice\n3.Water\n4.Exit")
            choice=int(input("What you want to choose(1-4)"))
            if choice==1:
                 print("\n\nHere's your Coke\n\n")
            elif choice==2:
                 print("\n\nHere's your juice\n\n")
            elif choice==3:
                 print("\n\nHere's your Water\n\n")
            elif choice==4:
                print("Thank you for coming!")
                break
        
            else:print("Invalid choice, please select 1-4.")
        
           
        
            