'''
Assignment - 5
Print numbers from 1 to 100 
with 'Fizz' replacing multiples of 3, 
and 'Buzz' instead of multiples of 5

By: Amrithaa Seshadri 
'''

i=1

while(i<=100):
	if i%3==0 and i%5==0:
		print("FizzBuzz")
	elif i%5==0:
		print('Buzz')
	elif i%3==0:
		print('Fizz')
	else:
		print(i)
	i+=1

