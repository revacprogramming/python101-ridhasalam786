# Functions


h = int(input("Enter Hours:"))
r = float(input("Enter the rate per hour:"))

def computepay(h,r):
    if (h>40):
        gp = (40 * r) + ((h - 40) * 1.5 * r)
    else:
        gp=h*r
    return gp

gp = computepay(h,r)
print("Pay", gp)
