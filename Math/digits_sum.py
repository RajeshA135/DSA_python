#Sum of digits of a given number
def sum(num):
    tot=0
    for i in num:
        tot+=int(i)
    return tot  
        
num=input("Enter a Number:")
print(sum(num))