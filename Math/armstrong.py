#Armstrong Number :a number that is equal to the sum of its own digits each raised to the power of the total number of digits in the number
def armstrong(n):
    l=len(str(n))
    tot=0
    for i in str(n):
        tot+=int(i)**l
    if n==tot:
        print("Armstrong Number")
    else:
        print("not an Armstrong Number")
n=int(input("Enter a Number:"))
armstrong(n)
