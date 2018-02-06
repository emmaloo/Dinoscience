menu = """
1. Find Sum
2. Find Product
"""
print(menu)
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
