import random

lowest_num = 1
highest_num = 10

random_number = random.randint(lowest_num, highest_num)
attempt = 0
max_attempt = 5
correct_guess = False

print(f"Guess the correct number between {lowest_num}, and the {highest_num}")
print(f"You have {max_attempt} attempts to guess the correct number")

while attempt < max_attempt and not correct_guess:
    guess = int(input(" Guess the correct number: "))
    if guess < 1 or guess > 10:
        print("Out of range, please guess a number betwee 1 and ten")
        continue
    attempt += 1
    if guess == random_number:
        print(f"Congratulations, you guessed the correct number {random_number}, in {attempt}")
        correct_guess = True
    elif guess < random_number:
        print("Too low, try again")
    elif guess > random_number:
        print("Too high try again")

    # match guess:
    #     case _ if guess < random_number:
    #         print("Too low")
    #     case _ if guess > random_number:
    #         print("Too high")
    #     case _ if guess == random_number:
    #         print("Congratulations")

if not correct_guess:
    print(f"Sorry you have used all {max_attempt}, the correct number was {random_number}")



