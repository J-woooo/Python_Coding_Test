n = int(input())
n_list = list(map(int, input().split(" ")))
m = int(input())
m_list = list(map(int, input().split(" ")))

n_list.sort()

def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start>end:
        return False
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for item in m_list:
    if binary_search(n_list, item, 0, len(n_list)-1):
        print("yes", end=' ')
    else:
        print("no", end=' ')
