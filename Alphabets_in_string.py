str="Nagpur_440010"
count=0
print("The Original string: ",str)
print("The alphabets in given string are:")
for c in  str:
    if(c.isalpha()):
        print(c)
        count=count+1

print("Total number of charcter in string are:" ,count)