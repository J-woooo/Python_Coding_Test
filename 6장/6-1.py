n = int(input())
numbers = []
for i in range(n):
    number = int(input())
    numbers.append(number)
numbers.sort(reverse=True)
for number in numbers:
    print(number, end=' ')