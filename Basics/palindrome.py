#Check if a number is a palindrome
def is_palindrome_number(n):
    original = str(n)
    reversed_num = original[::-1]
    return original == reversed_num

n = int(input("Enter a number: "))
if is_palindrome_number(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")
