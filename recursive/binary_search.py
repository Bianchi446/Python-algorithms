def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data , target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


data = [1, 2, 3, 4, 5, 7, 6, 8, 9 , 11, 10, 12, 14, 13, 16, 14, 15 , 16, 19 ,20]

print(binary_search(data, 11, 4, 20))
