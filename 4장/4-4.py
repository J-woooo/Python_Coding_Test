# 오답:규칙3번에서 뒤로 빠지는 경우 구현 안했음
n, m = map(int, input().split())
A,B,d = map(int, input().split())
# 0:북, 1:동, 2:남, 3:서

visited = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
count = 1
# 0: 육지, 1: 바다

maps = []
for i in range(n):
  map_row = list(map(int, input().split()))
  maps.append(map_row)

def left_sight(A,B,d):
  if d == 0:
    A = A
    B -= 1
  elif d==1:
    A -= 1
    B = B
  elif d==2:
    A = A
    B += 1
  elif d==3:
    A += 1
    B = B
  return A,B


def turn_left(d):
  return (d+7)%4


def move_front(A,B,d):
  if d == 0:
    A -= 1
    B = B
  elif d==1:
    A = A
    B += 1
  elif d==2:
    A += 1
    B = B
  elif d==3:
    A = A
    B -= 1
  return A,B
def move_back(A,B,d):
  if d == 0:
    A += 1
    B = B
  elif d==1:
    A = A
    B -= 1
  elif d==2:
    A -= 1
    B = B
  elif d==3:
    A = A
    B += 1
  return A,B

def is_stop(A,B,d):
  if (visited[A+1][B] == 1 or maps[A+1][B] == 1) and (visited[A-1][B] == 1 or maps[A-1][B] == 1) and (visited[A][B+1] == 1 or maps[A][B+1] == 1) and (visited[A][B-1] == 1 or maps[A][B-1] == 1):
    return True
  else:
    return False

visited[A][B] = 1

while(1):
  if is_stop(A,B,d):
    break 
  left_A, left_B = left_sight(A,B,d)
  print("현재 좌표: ",A,B, "왼쪽시야: ",left_A, left_B, "방향: ", d)
  if visited[left_A][left_B] == 0 and maps[left_A][left_B] == 0: 
    #아직 가보지 않았다면 왼쪽으로 돌고 앞으로 이동
    d = turn_left(d)
    print(A,B,"에서", end=" ")
    A,B = move_front(A,B,d)
    print(A,B,"로 이동")
    count += 1
    visited[A][B] = 1
  elif visited[left_A][left_B] == 1 or maps[left_A][left_B] == 1:
    d = turn_left(d)
print(count)