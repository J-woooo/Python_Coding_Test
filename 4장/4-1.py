n = input()
commands = list(input().split())
# print(n)
# print(commands)

x = 1
y = 1

for command in commands:
  if command == 'R' and y != n:
    y += 1
  elif command =='U' and x != 1:
    x -= 1
  elif command == 'D' and y != n:
    x += 1
  elif command =='L' and y != 1:
    y -= 1
  else:
    pass
print(x, y)