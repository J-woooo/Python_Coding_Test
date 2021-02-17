# 오답이유: 같을 때만 구할 수 있고 최적의 절단 해를 구할 수 없다. 
n, m =map(int,input().split())
rice_cake = list(map(int, input().split()))
rice_cake.sort(reverse=True)
array = [i for i in range(rice_cake[0]+1)]

def cut(array, rice_cake, goal, start, end):
    mid = (start + end) // 2
    cutter = array[mid] # 9

    cut_rice_cake = [(r-cutter) for r in rice_cake if r >= cutter]
    result = sum(cut_rice_cake)

    if result == goal:
        return array[mid]
    elif result < goal:
        return cut(array, rice_cake, goal, start, mid-1)
    else:
        return cut(array, rice_cake, goal, mid+1, end)
print(cut(array, rice_cake, m, 0, len(array)-1))