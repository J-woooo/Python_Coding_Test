for test_case in range(1, T + 1):

    numList = list(map(int, input().split(" ")))
    sum = 0
    for num in numList:
        if num % 2 == 1:
            sum += num
    print(f"#{test_case} {sum}")
