# import random

# lowest_num = 1
# highest_num = 10

# random_number = random.randint(lowest_num, highest_num)

# attempt = 0
# max_attempts = 5
# correct_guess = False

# print(f"Guess the correct number between {lowest_num}, and {highest_num}")
# print(f"You have {max_attempts} attempts to guess the correct number")

# while attempt < max_attempts and not correct_guess:
#     guess = int(input("Guess the correct number: "))
#     if guess < 1 or guess > 10:
#         print("Out of range! Please guess a number between 1 and 10.")
#         continue

#     attempt += 1

#     if guess == random_number:
#         print(f"Congratulations! You guessed the correct number: {random_number}")
#         correct_guess = True
#     elif guess < random_number:
#         print(f"Too low, try again")
#     elif guess > random_number:
#         print(f"{guess} is too high, try again")

# if not correct_guess:
#     print(f"Sorry you have used all {max_attempts}, the correct number was {random_number}")


import random

lowest_num = 1
highest_num = 10

random_number = random.randint(lowest_num, highest_num)

attempt = 0
max_attempts = 5
correct_guess = False

print(f"Guess the correct number between {lowest_num}, and {highest_num}")
print(f"You have {max_attempts} attempts to guess the correct number")

while attempt < max_attempts and not correct_guess:
    guess = int(input("Guess the correct number: "))
    if guess < 1 or guess > 10:
        print("Out of range! Please guess a number between 1 and 10.")
        continue

    attempt += 1

    # if guess == random_number:
    #     print(f"Congratulations! You guessed the correct number: {random_number}")
    #     correct_guess = True
    # elif guess < random_number:
    #     print(f"Too low, try again")
    # elif guess > random_number:
    #     print(f"{guess} is too high, try again")

    match guess:
        case _ if guess < random_number:
            print("Too low!")
        case _ if guess > random_number:
            print("Too High")
        case _:
            print("Congratulations! You guessed the correct number: {random_number}")
            

if not correct_guess:
    print(f"Sorry you have used all {max_attempts}, the correct number was {random_number}")

