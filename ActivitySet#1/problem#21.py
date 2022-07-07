Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

try:
	h = float(hours)
	r = float(rate)
except:
	print ('Error, please enter numeric input')
	
if h>40:
    gp=(40*r)+((h-40)*1.5*r)
else:
    gp=h*r
print(gp)



