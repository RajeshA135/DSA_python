#finding Maximum number in an array
def max_array(arr):
    max=arr[0]
    for i in arr:
        if i> max:
            max=i
    print("Maximum number in an array is",max)
arr=list(map(int,input("Enter Elements:").split()))
max_array(arr)