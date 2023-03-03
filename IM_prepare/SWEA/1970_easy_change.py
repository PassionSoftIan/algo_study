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