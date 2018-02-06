n = int(input("What's your number?"))
sum = 0
for x in range(0,n + 1):
	if x % 3 or x % 5:
		sum = sum + x
		print(sum)
