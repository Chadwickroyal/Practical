import random
# Generate a random number between 1 and 20
random_number = random.randint(1, 20)

while True:
    #Ask the user to enter their guess

user_guess = int(input("Guess the number between 1 and 20: "))

#check if the guess is correct
    if user_guess == random_number:
        print("Hurray! You won. The correct number is", random_number)
        break
    elif user_guess < random_number:
        print("Your guess is too low,")
    else:
        print("Your guess is too high.")

    
