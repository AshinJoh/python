arr = [1, 5, 6, 2, 9,]
num = int(input("Enter number"))

def linear(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return True
    return False

print(linear(arr, num))

