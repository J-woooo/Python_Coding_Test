n = list(map(int, input()))

mid = int((len(n)/2)-1)
front = sum(n[:mid+1])
back = sum(n[mid+1:])
if front==back:
    print("LUCKY")
else:
    print("READY")