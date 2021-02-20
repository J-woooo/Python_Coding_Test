# 만들 수 없는 금액
n = int(input())
coin = list(map(int, input().split()))
coin.sort()
target = 1

for c in coin:
    if c <= target:
        target += c
        print(target, " <- ", c)
    else:
        break
print(target)