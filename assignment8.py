'''
ASSIGNMENT 8

By: Amrithaa Seshadri
'''
import os.path
import os 
import string

filename=input("Please enter the file name (with txt): ") 

if os.path.exists(filename)==True:	
	print("Your file exists. Here are your options: \n1. Read the file\n2.Delete the file and start over\n3. Append the file\n4. Replace a Single Line\n")
	in1=input("****PLEASE ENTER YOUR OPTION**** - ")
	in1=int(in1)
	if in1==1:
		print("---------\nReading Contents of your file!")
		readfile=open(filename,"r")
		text=readfile.read()
		print("Contents of your file are: ",text)
	if in1==2:
		print("---------\nDeleting your file!")
		os.remove(filename)
		print("Your file has been removed. Creating a new empty one in its place...")
		new=open(filename,"w")
		new.close()
	if in1==3:
		print("---------\nAppending Text to your file!")
		app=open(filename,"a")
		text=input("Enter the text you want to append: ")
		app.write("\n"+text)
		app.close()
		print("The text",text,"has been appended to your file",filename)
		with open(filename,'r') as rep:
			dat=rep.read()
			print(dat)
	if in1==4:
		print("---------\nReplacing a Single Line")
		
		num=int(input("Which line number do you want to update? "))
		chg=num-1
		text=input("Enter the text that should replace that line: ")
		with open(filename,'r') as rep:
			data=rep.readlines()
		data[chg]=text+"\n"
		print("\nLine number",num,"of the file has been replaced with the text: ",text)
		with open(filename,'w') as rep:
			rep.writelines(data)
		with open(filename,'r') as rep:
			dat=rep.read()
			print(dat)
		
else: 
	print("Your file doesn't exist. Creating a new file for you")
	filewrite=open(filename,"w")
	text=input("Please enter the text you want to write to the file: ")
	filewrite.write(text)
	print("Your text has been added to the file.")
	filewrite.close()
