# 모험가 길드
n = int(input())
array = list(map(int, input().split()))
array.sort()

result = 0
count = 0 

for i in range(len(array)):
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
