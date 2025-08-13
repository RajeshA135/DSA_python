#Checking if the array is sorted or not?
def sorted(arr):
    asc=True
    desc=True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            asc=False
        if arr[i]<arr[i+1]:
            desc= False
    if asc:
        return "Array is sorted in ascending order"
    elif desc:
        return "Array is sorted in descending order"
    else:
        return "Array is not sorted"
arr=arr=list(map(int,input("Enter Elements: ").split()))
print(sorted(arr))