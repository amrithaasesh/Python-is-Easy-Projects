'''
Assignment #3 
Create a function that accepts 3 parameters and checks for equality between any two of them. 

By: Amrithaa Seshadri 
'''

def check(a,b,c):
	if int(a)==int(b) and int(b)==int(c): #Checks if all three are equal
		return True
	elif int(a)==int(b) or int(b)==int(c) or int(a)==int(c): #Checks for equality between any two variables 
		return True 
	else:
		return False

a=1
b=2
c='3'

out=check(a,b,c)

if out==1:
	print("Two or more variables are equal")
else:
	print("The variables aren't equal")