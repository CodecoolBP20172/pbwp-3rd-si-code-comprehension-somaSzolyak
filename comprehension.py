# searches the random module then binds it in the local (name)scope
import random

# initializes the guess taken variable with 0
guessesTaken = 0

# prints a string in the terminal
print('Hello! What is your name?')
# saves the user's imput into the myName variable
myName = input()

# assings a random number between 1 and 20 to the 'number' variable
number = random.randint(1, 20)
# prints 2 strings into the terminal with the myName varible in between them
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

# this is a loop that runs as long as the guessTaken veriable is less then 6
while guessesTaken < 6:
    # prints a string to the terminal
    print('Take a guess.')
    # saves the users imput into the gues variable
    guess = input()
    # converts the guess variable into an decimal numberm(from a string as the input() function returns a string)
    guess = int(guess)

    # increases the guessTaken variable by 1
    guessesTaken += 1

    # is the guess variable is smaller then the number variable prints something
    if guess < number:
        print('Your guess is too low.')

    # if the guess variable is bigger then the number variable prints something
    if guess > number:
        print('Your guess is too high.')

    # if the guess variable is equal to the number variable then breaks the loop
    if guess == number:
        break

# if the guess variable is equal to the number variable
# prints out a message with the number of guesses taken and the users name
if guess == number:
    # converts the guessesTaken variable to a string
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

# if the guess variable is not equal to the number variable
# converts the number variable into a string and prints a message with the number variable in it
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
