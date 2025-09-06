#Perfect Number: Sum of divisors equal to that number
def perfect(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
           sum+=i
    if sum==n:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
n=int(input("Enter a Number:")) 
perfect(n)