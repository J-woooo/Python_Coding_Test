# insertion sort
array1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array1)):
    min_index = i
    for j in range(i + 1, len(array1)):
        if array1[min_index] > array1[j]:
            min_index = j
    array1[i], array1[min_index] = array1[min_index], array1[i]
print(array1)

# selection sort
array2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
size = len(array2)
for i in range(size):
    for j in range(i, 0, -1):
        if array2[j] < array2[j - 1]:
            array2[j], array2[j - 1] = array2[j - 1], array2[j]
        else:
            break
print(array2)

# quick sort
array3 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array3, 0, len(array3) - 1)
print(array3)

array4 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort_python(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)


array4 = quick_sort_python(array4)
print(array4)

# Counting sort
array5 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array5) + 1)

for i in range(len(array5)):
    count[array5[i]] += 1
print("[", end='')
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=', ')
print("]")

# by sorted
array6 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array6)
print(result)
