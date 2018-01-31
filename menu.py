#We're going to implement scripts from the elementary list on https://adriann.github.io/programming_problems.html
#    1 Print ‘Hello World’ to the screen.
#    2 Ask the user for their name and greet them with their name.
#    3 Ask the user for a number n and print the sum of the numbers 1 to n
#    4 The previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
#    5 Ask the user for a number n and give them the possibility to choose between computing the sum and computing the product of 1,…,n.
#    6 Write a program that prints a multiplication table for numbers up to 12.
#    7 Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. I counts only as one try if they input the same number multiple times consecutively.

import roaden
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

    if choice == '1':
        roaden.helloworld()
    elif choice == '8':
        break
    else:
print("Invalid choice...")
