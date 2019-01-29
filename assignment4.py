'''
ASSIGNMENT-4

By: Amrithaa Seshadri
'''

myUniqueList=[]
myLeftovers=[]

def add(item):   #Checking if Item exists in List
		if item in myUniqueList:
			myLeftovers.append(item)
			return False
		else:
			myUniqueList.append(item)
			return True

def check(x,var): #Based on the return value, a display message is given
	if var==0:
		print(x,"was entered. Value already exists on the list, so it wasn't added")
	else:
		print(x," is a New value and has been added to the list")

item=[1,"Amrithaa",3,"World",1,"Amrithaa",4,5,3,"Hello"] #A LIST OF ALL THE VALUES. SOME HAVE BEEN REPEATED, TO CHECK THE EFFICIENCY OF CODE

for x in item:
	var=add(x)
	check(x,var)

print("My Unique List is: ", myUniqueList) #Printing Unique and Leftover List
print("The leftovers are: ", myLeftovers)
