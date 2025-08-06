#Print Fibonacci series up to N terms
def fibonacci(n):
    if n<=0:
        print("No terms to display")
    elif n==1:
        print("0")
    elif n==2:
        print("0 1")
    else:
        num1,num2=0,1
        print(num1,num2,end=' ')
        for _ in range(n-2):
            num3=num1+num2
            print(num3,end=' ')
            num1,num2=num2,num3
        
           
n=int(input("Enter a number of terms:"))
fibonacci(n)
    
