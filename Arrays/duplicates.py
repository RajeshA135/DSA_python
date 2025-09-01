def remove_duplicates(arr):
    if not arr:
        return 0
    
    # Pointer for the position of unique elements
    i = 0
    
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    
    return i + 1  # length of unique elements

# Example
arr =sorted(list(map(int, input().split())))
length = remove_duplicates(arr)
print(length)         # 4
print(arr[:length])  # [1, 2, 3, 4]
