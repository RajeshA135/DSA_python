#Check if a number is prime
def is_prime(n):
    if n <= 1:
        return "Not a prime"
    if n == 2:
        return "Prime"
    if n % 2 == 0:
        return "Not a prime"
    for d in range(3, int(n**0.5) + 1, 2):
        if n % d == 0:
            return "Not a prime"
    return "Prime"
n=int(input("Enter a number:"))
print(is_prime(n))