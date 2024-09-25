def merge(arr):
     if len(arr) <= 1:
          return arr
     
     mid = len(arr) // 2

     left = arr[:mid]
     right = arr[mid:]

     merge(left)
     merge(right)
     mergeSort(arr, left, right)

def mergeSort(arr, left, right):
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [1,5,4,2,7,6,0]
merge(arr)
print(arr)