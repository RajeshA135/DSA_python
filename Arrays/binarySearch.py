# Searching an element using binary search with O(log n) time complexity
def binary_search(arr,target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"Element found at index: {mid}"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return "Element not found"
arr=sorted(list(map(int,input("Enter array Elements: ").split())))
target=int(input("Enter search Element:"))
print("sorted array:",arr)
print(binary_search(arr,target))