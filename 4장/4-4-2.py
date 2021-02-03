n,m = map(int, input().split())
x, y, direction = map(int, input().split())
maps = []
for i in range(n):
  mapRow = list(map(int, input().split()))
  maps.append(mapRow)
print(maps)

# n, m = 4, 4
# x, y, direction = 1, 1, 0
# maps = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]

visited = [[0] * n for _ in range(m)]
visited[x][y] = 1

def turnLeft():
  global direction
  direction -= 1
  if direction < 0:
    direction = 3

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 시뮬레이션 시작
count = 1
turn_time = 0
while(1):
  # 왼쪽으로 회전
  turnLeft()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if visited[nx][ny] == 0 and maps[nx][ny] == 0:
    visited[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    # print(x,y, direction, turn_time)
    continue
    # 회전한 이후 정면에 가보죄 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
    # print(x,y, direction, turn_time)
  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동하기
    if maps[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0

print(count)