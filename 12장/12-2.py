array = list(input())


def isNum(number):
    if number == '0' or number == '1' or number == '2' or number == '3' or number == '4' or number == '5' or number == '6' or number == '7' or number == '8' or number == '9':
        return True
    return False


alphabet = []
sum = 0
for number in array:
    if isNum(number):
        sum += int(number)
    else:
        alphabet.append(number)
alphabet.sort()
if sum != 0:
    alphabet.append(sum)
print(''.join(alphabet))
