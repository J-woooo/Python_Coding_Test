# m,n = map(int, input().split())
# a, b, dir = map(int, input().split())
# maps = []
# for i in range(n):
#   mapRow = list(map(int, input().split()))
#   maps.append(mapRow)
# print(maps)

m, n = 4, 4
a, b, div = 1, 1, 0
maps = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]

visited = [[0] * n for _ in range(m)]
visited[a][b] = 1
# print(visited)
count = 1
def turnLeft(div):
  result = div - 1
  if result < 0:
    result = 3
  return result

da = [-1,0,1,0]
db = [0,1,0,-1]

left = turnLeft(div)

# 왼쪽 방향 안가봤으면 왼쪽 회전하고 한칸 전진
rotate = 0
while(1):
  if rotate == 4:
    if maps[a-da[div][b-da[div]]] == 1:
      break
    else:
      a -= da[div]
      b -= da[div]
      rotate = 0


  if visited[da[left]] == 0 and maps[da[left]] == 0:
    print(a,b,"에서",end=" ")
    a += da[div]
    b += db[div]
    print(a,b,"로 이동")    
    visited[a][b] = 1
    div = left
    left = turnLeft(div)
    rotate = 0
    count += 1
  # 왼쪽이 갈수없는길이면 회전만 함
  if visited[da[left]] == 0 and maps[da[left]] == 1:
    div = left
    left = turnLeft(div)
    rotate += 1
  # 왼쪽 방향 안가봤으면 왼쪽 회전하고 한칸 전진

print(count)