# 곱하기 혹은 더하기
num_list = list(map(int, input()))
# print(num_list)

result = 0

for number in num_list:
    sum = result + number
    mul = result*number
    result = (max(sum, mul))
print(result)