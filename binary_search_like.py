

array = [6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5]

def binary_search_like(array, value):
    """mixture binary search like"""
    if len(array) == 0:
        return -1
    elif len(array) == 1:
        return 0 if array[0] == value else -1

    left = 0
    right = len(array) - 1
    while True:
        # break condition
        if left > right:
            return -1
        elif left == right:
            return left if array[left] == value else -1

        middle = (right + left) // 2
        if array[middle] == value:
            return middle
        elif array[left] <= array[middle]:
            # asc in left
            if value >= array[left] and value < array[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            # asc in right
            if value > array[middle] and value <= array[right]:
                left = middle + 1
            else:
                right = middle - 1
