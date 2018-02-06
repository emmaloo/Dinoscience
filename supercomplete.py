menu = """
        Pick a menu option!
---------------------------------------------------------
	1 Say 'Hello World'
	2 Ask your name, and greet you
	3 Find the sum from 1 to n
	4 Find the sum from 1 to n that are multiples of 3 or 5
	5 Find the product from 1 to n
	6 Print a multiplication table to 12
	7 Play a guessing game
	8 Choose sum y product
	"""
print(menu)
choice = input()

if choice == "1":
	print("Hello cruel world!")
elif choice == "2":
	name = input('Enter your name: ')
	print("Welcome", name)
elif choice == "3":
	n=int(input("Enter a number: "))
	sum1 = 0
	while(n > 0):
		sum1=sum1+n
		n=n-1
	print("That was easy! The sum is",sum1)
elif choice == "4":
	n = int(input("What's your number?"))
	sum = 0
	for x in range(0,n + 1):
		if x % 3 or x % 5:
			sum = sum + x
	print(sum)
elif choice == "5":
	n = int(input("What's your number"))
	product = 1
	while (n > 0):
		product = product * n
		n = n - 1
	print("Your product is", product)
elif choice == "6":
	n=int(input('Please enter a positive integer between 1 and 12: '))
	for row in range(1,n+1):
		print(*("{:3}".format(row*col) for col in range(1, n+1)))
elif choice == "7":
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

elif choice == "8":
	menu2 = """
	1. Find Sum
	2. Find Product
	"""
	print(menu2)
	choice = input()

	if choice == '1':
		n=int(input("Enter a number: "))
		sum1 = 0
		while(n > 0):
			sum1=sum1+n
			n=n-1
		print("That was easy! The sum is",sum1)

	elif choice == '2':
		n = int(input("What's your number"))
		product = 1
		while (n > 0):
			product = product * n
			n = n - 1
	print("Your product is", product)
