n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1 # 현재 그룹의 공포도
    if count >= i:
        result += 1
        count = 0
print(result)