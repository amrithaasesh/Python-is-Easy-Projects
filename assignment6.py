'''
Assignment-6
I have tried to create a Chess-Board, using '++' for the black spaces.
After testing, I have restricted the n(rows) and n(columns) to be 20
'''

def board(rows,col):
	if rows<=20 and col<=20:
		for i in range(1,rows+1,1):
			if i%2!=0:
				for j in range(1,col+1,1):
					if j%2!=0:
						print("  ",end="  ")
					else:
						print("++",end="  ")
			else:
				for j in range(1,col+1,1):
					if j%2!=0:
						print("++",end="  ")
					else:
						print("  ",end="  ")
			print("\n")
		return True
		
	else: 
		return False


output=board(5,5)

if output==True:
	print("\n\nYour chessboard has been created successfully")
else:
	print("Invalid Dimensions. Enter rows and column value below 20")




