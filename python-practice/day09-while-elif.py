# atm simulation
balance=1000

while True:
    command=input("enter command:")
    if command=="balance":
        print(balance)
         
    elif command=="deposit":
        deposit=int(input("enter deposit: "))
        balance=deposit+balance
        print(balance)
        
    elif command=="withdraw":
        withdraw=int(input("enter withdraw: "))
        balance = balance - withdraw
        print(balance)
    elif command == "exit":
        print("Exiting the program...")
        break
        
    else:
        print("Invalid command, try again.")