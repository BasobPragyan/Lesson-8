a=int(input("Enter numerator"))
b=int(input("Enter denominator"))
if (a%b==0):
    print("{0} is divisible by {1}".format(a,b))
else:
    print("{0} is not divisible by {1}".format(a,b))