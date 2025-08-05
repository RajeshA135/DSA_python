#Swap two numbers without using a third variable
def swap_numbers(a,b):
    print("before swapping:",a,b)
    a,b=b,a #main logic
    print("after swapping:",a,b)
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print(swap_numbers(a,b))