# n 크기
# m 횟수
# k 숫자
n, m, k = map(int, input().split())
numList = list(map(int, input().split()))
# print(n,m,k)
# print(numList)
result = 0
numList.sort()

for i in range(m):
  if (i % 3 == 0) and (i != 0):
    result += numList[n-2]
  else:
    result += numList[n-1]
print(result)