#Program to check if a number is divisible by 3 and 5
num1 = int(input("Enter a number :"))
ans1 = num1 % 3
ans2 = num1 % 5

if(ans1 == 0):
	print(num1 , " is divisible by 3")
else :
	print(num1 , " is not divisible by 3")

if(ans2 == 0):
	print(num1 , " is divisible by 5")
else:
	print(num1 , " is not divsible by 5")

