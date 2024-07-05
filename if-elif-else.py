#Program to check if a number is single digit
# double digit or triple digit
num1 = int(input("Enter a number"))
if(num1 >=0 and num1 <= 9):
	print(num1 ," is single digit")

elif(num1 >=10 and num1 <=99):
	print(num1, " is double digit")

elif(num1 >=100 and num1 <= 999):
	print(num1 ," is triple digit")
else:
	print(num1 ,"is neither single, nor double nor triple")

