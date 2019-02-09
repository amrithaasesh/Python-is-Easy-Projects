Song1={'Name':'All of Me','Artist':'John Legend','Album':'Love in the Future','time':269,'Release':'August 12, 2013'}

def songprint(userkey):
   for key in Song1:
        print(key,': ',Song1[key])


def checksong(userkey):
    if userkey in Song1.keys():
        print("You guessed correct. Here are all the entries corresponding to that!")
        songprint(userkey)
        return True
    else:
        print("You entered a wrong entry. It doesn't exist in our dictionary")
        return False

userkey=str(input('What parameter would you like to search for? '))
output=checksong(userkey)




