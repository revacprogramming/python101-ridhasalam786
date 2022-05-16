# Conditional Execution
hrs = input("Enter Hours:")
h = int(hrs)
rate = input("Enter the rate per hour:")
r = float(rate)
if h>40:
    gp=(40*r)+((h-40)*1.5*r)
else:
    gp=h*r
print(gp)