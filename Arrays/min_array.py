#finding minimum number in an array
def min_array(arr):
    min=arr[0]
    for i in arr:
        if i< min:
            min=i
    print("Minimum number in an array is",min)
arr=list(map(int,input("Enter Elements:").split()))
min_array(arr)