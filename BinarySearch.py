def bsearch(arr, target):    
    # write your code here

    # for idx, number in enumerate(arr):
    #     if number == target:
    #         return idx
    #         break

    first = 0
    last = len(arr)-1
    
    while first<=last:
        mid = int (first + (last-first)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return -1
 
x = [7,9,21,42,58,67,88] 
print(bsearch(x, 67) == 5)
print(bsearch(x, 9) == 1)