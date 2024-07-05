# Print the grade of a student based on the percentage
# Take input as marks for 3 subjects
# find the percentage
# if perc is greater than 75 then grade is A+
# if perc is between 65 and 75 then grade is A
# if perc is between 55  and 64 then grade is B
# if perc is between 40 and 54 then grade is C
# if perc is less than 40 then grade is D else fail
marks1 = int(input("Enter the marks for Python:"))
marks2 = int(input("Enter the marks for Java Programming :"))
marks3 = int(input("Enter the marks for Android :"))
total = marks1 + marks2 + marks3
perc = total/3
if(perc >75):
	print("A+")
elif(perc >= 65 and perc <=75 ):
	print("A")
elif(perc>= 55 and perc <=64):
	print("B")
elif(perc >= 40 and perc <=54):
	print("C")
elif(perc <40):
	print("D")
else:
	print("Fail")