import random

def guess():
    number = int(input("Enter a number: "))
    random_number = random.randint(1, number)
    user_guess = 0

    while user_guess != random_number:
        user_guess = int(input(f"Enter your guess between 1 and {number}: "))
        if user_guess < random_number:
            print("Your guess is lower than the correct number. Please guess again.")
        elif user_guess > random_number:
            print("Your guess is higher than the correct number. Please guess again.")

    print(f"Congrats! You guessed the correct number which is {random_number}")

    user_response = input("Wanna play again? 'yes' or 'no': ").lower()

    if user_response == 'yes':
        guess()
    elif user_response == 'no':
        print("Come again sometime :)")
    else:
        print("Invalid response.")

def computer_guess():
    highest_number = int(input("Enter a number for determining the range of guessing: "))
    lowest = 1
    highest = highest_number

    guess = random.randint(lowest, highest)
    determining = ''

    while determining != 'C':
        determining = input(f"Is {guess} too high ('H')? Too low ('L') or correct ('C')? ").upper()
        if determining == 'H' or determining == 'L':
            guess = random.randint(lowest, highest)
            continue

        print(f"Computer guessed correctly the number {guess}")

    user_response = input("Wanna play again? 'yes' or 'no': ").lower()

    if user_response == 'yes':
        computer_guess()
    elif user_response == 'no':
        print("Come again sometime :)")
    else:
        print("Invalid response.")

#guess()
computer_guess()