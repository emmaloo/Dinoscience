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
	8 Exit
	"""

while(True):
	 print(menu)


choice = input()

if choice == "1":
	from compiled import *
	question1()
elif choice == "8":
	break
elif choice == "2":
	from compiled import *
	question2()
elif choice == "3":
	from compiled import *
	question3()
elif choice == "4":
	from compiled import *
	question4()
elif choice == "5":
	from compiled import *
	question5()
elif choice == "6":
	from compiled import *
	question6()
elif choice == "7":
	from compiled import *
	question7()
elif choice == "8":
	from compiled import *
	question8()
