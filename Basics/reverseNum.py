#Reverse a number
def reverse(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    print(rev)
num=int(input("Enter a number:"))
reverse(num)