# 효율적인 화폐 구성
n, m = map(int, input().split(" "))

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)
d[0] = 0
print(d)

for money in array:
    if money > m:
        break
    d[money] = 1
    for i in range(money, m + 1):
        d[i] = min(d[i], d[i-money] + 1)
    print(d)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])