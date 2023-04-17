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

# type(arr) = list; type(num) = int;
