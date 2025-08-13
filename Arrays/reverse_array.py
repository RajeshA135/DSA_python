#Reverse an Array using Recursion
def reverse_array(arr, start , end):
    if start>=end:
        return 
    arr[start],arr[end]=arr[end],arr[start]
    reverse_array(arr, start+1, end-1)
    return arr
arr=list(map(int,input("Enter Elements: ").split()))
print("Input array:",arr)
print("Reversed Array:",reverse_array(arr,0,len(arr)-1))
# Slicing
array=[1,2,3,4,5,6]
print("Reversed array:",array[::-1])