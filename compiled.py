def question1():
	print("Hello cruel world!")

def question2():
	name = input('Enter your name: ')
print("Welcome", name)

def question3():
n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("That was easy! The sum is",sum1)

def question4():
n = int(input("What's your number?"))
sum = 0
for x in range(0,n + 1):
	if x % 3 or x % 5:
		sum = sum + x
		print(sum)
def question5():
n = int(input("What's your number"))
product = 1
while (n > 0):
	product = product * n
	n = n - 1
print("Your product is", product)

def question6():
n=int(input('Please enter a positive integer between 1 and 12: '))
for row in range(1,n+1):
    print(*("{:3}".format(row*col) for col in range(1, n+1)))

def question7():
import random

def play_again():
    while True:
        replay = input('Play again? Yes or No?\n')
        if replay.lower() == 'yes':
            return True
        elif replay.lower() == 'no':
            return False
        print('Invalid input.')

def main():
    print('Welcome to the number guess game!', end='\n\n')

    random_number = random.choice(range(1, 101))

    print("I'm thinking of a number which is between 1 and 100 (amazing). Can you guess it?")

    guesses, guess = 0, 0

    while guess != random_number:
        try:
            guess = int(input("Enter a number: "))
        except:
            print('Invalid input.')
            continue
        if guess > random_number:
            print('Too high. Guess lower.')
        elif guess < random_number:
            print('Too low. Guess higher.')
        guesses+=1
    print('Congratz. You guessed my number {0} in {1} guesses'.format(random_number, guesses))

    if play_again():
        main()
    else:
        print('Seeya loser!')

main()

def question8():
	if input = 8:
	break
