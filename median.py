# cal median
import random

arr1 = random.sample(range(10), 10)
print("arr1 =", arr1)

arr2 = random.sample(range(10, 20), 10)
print("arr2 =", arr2)

arr3 = arr1 + arr2

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

arr3 = quicksort(arr3)
print(arr3)

if len(arr3) % 2 == 0:
    median = (arr3[len(arr3) // 2] + arr3[len(arr3) // 2 - 1]) / 2
else:
    median = arr3[len(arr3) // 2]

print("Median =", median)
