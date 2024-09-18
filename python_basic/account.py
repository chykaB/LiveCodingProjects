# Pseudoceode for the Bank account activity 
# Step1. Set initial balance
# Step2. Show users options: Check balance, Withdraw, Deposit, exit
# Step3. User input:
    #if check, display the current balance
    #if deposit, ask for the amount add it to the balance, display the new balance
    #if withdraw, ask for the amount, 
        #check if their balance is sufficient, subtract the amount from their balance if not sufficient we display a message.
#step 4 Repeat process

balance = 0

# Show options
while True:
    print("Select an option")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    option = input("Enter option number:  ")

    if option == "1":
        print(f"Your current balance is ${balance}")
    elif option == "2":
        deposit_amount = int(input("Enter the amount: "))
        balance += deposit_amount
        print(f"You have successfully deposited {deposit_amount}. New balance ${balance}")
    elif option == "3":
        withdraw_amount = int(input("Enter amount"))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"You hav successfully withdrawn {withdraw_amount}. new balance ${balance}")
        else:
            print("Insufficient fund")
    elif option == "4":
        print("THank you goodbye")
        break
        
    else:
        print("Invalid option")

