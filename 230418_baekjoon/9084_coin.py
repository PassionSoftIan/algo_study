import sys
sys.stdin = open('9084_coin_input.txt')

Test_case = int(input())

for tc in range(1, Test_case+1):
    N = int(input())
    coin = list(map(int, input().split()))
    money = int(input())

    DP = [0] * (money + 1)
    DP[0] = 1

    for c in coin:
        for i in range(c, money + 1):
            DP[i] += DP[i-c]

    print(DP[money])