# Searching an element linearly with O(n) time complexity
def linear_search(n, arr):
    for index, value in enumerate(arr):
        if n == value:
            return f"Element found at index: {index}"
    return "Element not found"

arr = list(map(int, input("Enter array elements: ").split()))
n = int(input("Enter search element: "))
print(linear_search(n, arr))
