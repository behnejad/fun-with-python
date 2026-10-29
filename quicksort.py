import random
import time

def delta(func):
    def wrap(*x):
        a = time.time()
        res = func(*x)
        print(time.time() - a)
        return res

    return wrap

def qsort(array):
    if len(array) == 1 or len(array) == 0:
        return array
    if len(array) == 2:
        if array[0] > array[1]:
            return array[::-1]
        else:
            return array

    index = len(array) // 2
    mid = array[index]
    arr1 = []
    arr2 = []
    arr3 = []
    for x in array:
        if x < mid:
            arr1.append(x)
        elif x > mid:
            arr2.append(x)
        else:
            arr3.append(x)

    #print(">", arr1, arr3, arr2)
    arr1 = qsort(arr1)
    arr2 = qsort(arr2)
    return [*arr1, *arr3, *arr2]

@delta
def mysort(x):
    return qsort(x)

@delta
def defsort(x):
    return sorted(x)

def test(array):
    t = mysort(array)
    s = defsort(array)
    #print(t)
    #print(s)
    print(t == s)
    #print()

if __name__ == '__main__':
    test([1])
    test([2, 1])
    test([1, 3, 2])
    test([0, 0, 1, 3])
    test([10, 9, 7, 6, 1, 0, 6, 5, 4, 3, 10, 22])
    test([0, 1, 0, 0, 0, 0, 5])
    for _ in range(100):
        test([random.randint(-10000, 10000) for _ in range(random.randint(1, 10000))])
