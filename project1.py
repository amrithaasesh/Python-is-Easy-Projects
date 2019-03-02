'''
PROJECT-1 
DRAW A CONNECT-4 BOARD

BY: Amrithaa Seshadri 
'''

#DRAWS THE FIELD AFTER EVERY ITERATION
def drawfield(field): 
	for row in range(12):
		if row%2==0:
			pracrow=int(row/2)
			
			for column in range(13):
				if column%2==0:
					praccol=int(column/2)
					if column!=12:
						print(field[praccol][pracrow],end="")
					else:
						print(field[praccol][pracrow])
					
				else:
					print("|",end="")
		else:
			print("-------"*2)

#CHECKING WINNING CONDITION FOR COLUMNS
def checkcol(currentfield):
	pl1=['X','X','X','X']
	pl2=['O','O','O','O']
	

	for col in range(7):
		for row in range(5,2,-1):	
			count=4
			r=row
			list=[]
			while count>0:
				list.append(currentfield[col][r])
				r-=1
				count-=1
			if list==pl1:
				print("Player 1 has won! Congratulations!")
				globals()["flag"]=1
				return
			elif list==pl2:
				print("Player 2 has won! Congratulations!")
				globals()["flag"]=1
				return

#CHECKING WINNING CONDITION FOR ROWS
def checkrow(currentfield):
	pl1=['X','X','X','X']
	pl2=['O','O','O','O']
	

	for row in range(6):
		for col in range(4):	
			count=4
			r=col
			list=[]
			while count>0:
				list.append(currentfield[r][row])
				r+=1
				count-=1
			if list==pl1:
				print("Player 1 has won! Congratulations!")
				globals()["flag"]=1
				return
			elif list==pl2:
				print("Player 2 has won! Congratulations!")
				globals()["flag"]=1
				return

#CHECKING WINNING CONDITION FOR DIAGONALS
def checkdiag(currentfield):
	pl1=['X','X','X','X']
	pl2=['O','O','O','O']
	

	for col in range(4):
		for row in range(3):	
			count=4
			c=col
			r=row
			list=[]
			while count>0:
				list.append(currentfield[c][r])
				r+=1
				c+=1
				count-=1
			
			if list==pl1:
				print("Player 1 has won! Congratulations!")
				globals()["flag"]=1
				return
			elif list==pl2:
				print("Player 2 has won! Congratulations!")
				globals()["flag"]=1
				return
	for col in range(6,2,-1):
		for row in range(3):	
			count=4
			c=col
			r=row
			list=[]
			while count>0:
				list.append(currentfield[c][r])
				r+=1
				c-=1
				count-=1
			
			if list==pl1:
				print("Player 1 has won! Congratulations!")
				globals()["flag"]=1
				return
			elif list==pl2:
				print("Player 2 has won! Congratulations!")
				globals()["flag"]=1
				return
		
currentfield=[[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
player=1
print("0|1|2|3|4|5|6|")
drawfield(currentfield)
r=[5,5,5,5,5,5,5]
out="True"
flag=0

#TAKING INPUT FROM THE USER, DISPLAYING THE BOARD, AND CHECKING FOR RESULTS
while(flag==0):
	print("Player Turn: ",player)
	movecol=int(input("Please enter the col (0 to 6): "))
	print("0|1|2|3|4|5|6|")
	if player==1:
		if r[movecol]>=0:
			if currentfield[movecol][r[movecol]]==" ":
				currentfield[movecol][r[movecol]]="X"
				r[movecol]-=1
				player=2
				drawfield(currentfield)
				
			else: 
				print("You cannot overwrite!")
		else:
			print("Try another column. This one is full")
	else:
		if r[movecol]>=0:
			if currentfield[movecol][r[movecol]]==" ":
				currentfield[movecol][r[movecol]]="O"
				r[movecol]-=1
				player=1
				drawfield(currentfield)
				
			else: 
				print("You cannot overwrite!")
		else:
			print("Try another column. This one is full")
	
	checkcol(currentfield)
	checkrow(currentfield)
	checkdiag(currentfield)
	
print("Thanks for playing the game")
	