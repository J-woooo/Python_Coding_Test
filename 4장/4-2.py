# 시간이 3일때와 아닌 경우로 나누어서 접근
# 시간이 3일때: 모든 분/초 카운트
# 시간이 3이 아닐 때: 3이 최소 한개 이상 포함되는 경우 카운트
n = int(input())

count = 0

for i in range(n+1):
  if i == 3:
    count += (60*60)
  else:
    count += (60*15*2 - 15*15)
print(count)