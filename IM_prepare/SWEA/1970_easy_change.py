import sys
sys.stdin = open('1970_easy_change_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    count = [0] * 8
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    # while N != 0:
    for i in range(len(money)):
        if N >= money[i]:
            while N >= money[i] and N != 0:
                N = N - money[i]
                count[i] += 1
    print(f'#{tc}')
    print(*count)






    # if N >= 50000:
    #     while N >= 50000:
    #         count[0] += 1
    #         N = N - 50000
    #
    #
    #
    # if N == 0:
    #     print(*count)
    #     continue
    #
    # if N >= 10000:
    #     while N >= 10000:
    #         count[1] += 1
    #         N = N - 10000
    # if N == 0:
    #     print(*count)
    #     continue
    #
    # if N >= 5000:
    #     while N >= 5000:
    #         count[2] += 1
    #         N = N - 5000
    # if N == 0:
    #     print(*count)
    #     continue
    #
    # if N >= 1000:
    #     while N >= 1000:
    #         count[3] += 1
    #         N = N - 1000
    # if N == 0:
    #     print(*count)
    #     continue
    #
    # if N >= 500:
    #     while N >= 500:
    #         count[4] += 1
    #         N = N - 500
    # if N == 0:
    #     print(*count)
    #     continue
    #
    # if N >= 100:
    #     while N >= 100:
    #         count[5] += 1
    #         N = N - 100
    # if N == 0:
    #     print(*count)
    #     continue
    #
    # if N >= 50:
    #     while N >= 50:
    #         count[6] += 1
    #         N = N - 50
    # if N == 0:
    #     print(*count)
    #     continue
    #
    # if N >= 10:
    #     while N >= 10:
    #         count[7] += 1
    #         N = N - 10
    # if N == 0:
    #     print(*count)
    #     continue