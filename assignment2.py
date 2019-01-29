'''
ASSIGNMENT-2: Use of functions to return the values of the song metadata
By: Amrithaa Seshadri 
'''

name="All of Me"
artist="John Legend"
album="Love in the Future"
time=269 #Run-time of the song
Release="August 12, 2013"
Funfact="It was shot in Italy, just days before Legend's wedding. It's his love song"

def songname():
	return name 

def songartist():
	return artist

def songalbum():
	return album 

def songtime():
	return time

def songrelease():
	return Release

def fact():
	return Funfact

def checkname(givename):
	if(givename == name):
		return True
	else:
		return False

def output(var):
	if var==1:
		print("You've entered the correct song name")
	else:
		print("Sorry, Incorrect Name")

print('##########################################\n')
print('SONG:',songname(), "by", songartist(),"\n")
print('##########################################\n')
print("Album:", songalbum(), "\n")
print("Length of the Song: (secs) ", songtime(), "\n")
print("Release Date: ", songrelease(),'\n')
print("DID YOU KNOW?", fact(), "\n")


var=checkname("ABCD")
print("Checking if song name is ABCD:")
output(var)


var=checkname("All of Me")
print("Checking if song name is All of Me:")
output(var)