def linear_search(n,arr):
    for i in arr:
        if n==i:
            return "Element is found"
    else:
            return "Element is not found"
arr=list(map(int,input("Enter array Elements: ").split()))
n=int(input("Enter search Element:"))
print(linear_search(n,arr))