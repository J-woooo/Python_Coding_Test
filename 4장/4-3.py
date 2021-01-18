i = input()

x, y = i[0], int(i[1])
# a 1
count = 0

x_list = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
# print(x_list[x], y)
move_x = [-1, -1, -2, -2, 1, 1, 2, 2]
move_y = [2, -2, 1, -1, 2, -2, 1, -1]

for i in range(8):
  dx = x_list[x] + move_x[i]
  dy = y + move_y[i]
  if dx < 1 or dx > 8 or dy < 1 or dy > 8:
    continue
  else:
    count += 1
print(count)