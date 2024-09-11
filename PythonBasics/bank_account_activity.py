# # Set the initial balance
# balance = 0

# #show options
# print("Select an option: ")
# print("1. Check balance")
# print("2. Deposit Money")
# print("3. Withdraw Money")
# print("4. Exit")

# option = input("Enter option number: ")

# if option == "1":
#     print(f"Your current balance is ${balance}")

# elif option == "2":
#     deposit_amount = float(input("Enter the amount you want to deposit: $"))
#     balance += deposit_amount
#     print(f"You have successfully deposited ${deposit_amount} your current balance is ${balance}")    
# elif option == "3":
#     withdraw_amount = float(input("Enter the amount you want to withdraw: $"))
#     if withdraw_amount <= balance:
#         balance -= withdraw_amount
#         print(f"You have successfully withdrawn ${withdraw_amount} your new balance is ${balance}")
#     else:
#         print("Insufficient fund")
# elif option == "4":
#     exit
#     print("Thank you and goodbye")
# else:
#     print("Invalid option try again")

# with while loop
balance = 0

while True:
    print("\nSelect an option")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("Exit")

    option = input("Enter an option number: ")

    if option == "1":
        print("Your current balance is ${balance}")

    elif option == "2":
        deposit_amount = int(input("Enter amount to deposit: $"))
        balance += deposit_amount
        print(f"Deposited ${deposit_amount} is successful. New balance ${balance}")
    elif option == "3":
        withdraw_amount = int(input("Enter amount to deposit: $"))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"You have successfully withdrawn ${withdraw_amount}. New balance ${balance}")
        else:
            print("Insufficient fund")
    elif option == "4":
        print("Goodbye")
        break
    else:
        print("Invalid transaction.Try again")

