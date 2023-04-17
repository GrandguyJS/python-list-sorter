def test(arr, num):
    low = 0
    high = len(arr)-1
    while low < high:
        mid = (low+high) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            low = mid+1
        else:
            high = mid-1
    return -1


print(test([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], 14))