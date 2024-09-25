def binary(arr, n):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == n:
            return True
        elif arr[mid] > n:
            r = mid - 1
        else:
            l = mid + 1
    
    return False

arr = [1,2,3,4,5]
n = 2

print(binary(arr, n))