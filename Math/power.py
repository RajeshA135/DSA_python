#Power of a number
def power(n,p):
    pow=1
    while p!=0:
        pow*=n
        p-=1
    print("Power of a Number is:",pow)
n=int(input("Enter Base Number:"))
p=int(input("Enter Exponent Number:"))
power(n,p)
