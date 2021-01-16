# n 크기
# m 횟수
# k 숫자
n, m, k = map(int, input().split())
numList = list(map(int, input().split()))
# print(n,m,k)
# print(numList)
result = 0
numList.sort()

first = numList[-1]
second = first = numList[-2]

count = m//(k+1)*k + m%(k+1)

result += count*first
result += (m-count)*second
print(result)