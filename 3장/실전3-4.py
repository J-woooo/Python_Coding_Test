n, k = map(int, input().split())
# print(n, k)
count = 0

while (1):
  if n==1:
    break
  if not n%k == 0:
    n -= 1
    count += 1
  else:
    n /= k
    count += 1
print(count)