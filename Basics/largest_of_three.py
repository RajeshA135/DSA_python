def largest(a,b,c):
    if a>=b and a >= c:
        print(f"largest num is {a}")
    elif b>=a and b>=c:
        print(f"largest num is {b}")
    else:
        print(f"largest num is {c}")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
largest(a,b,c)