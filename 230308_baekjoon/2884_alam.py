import sys
sys.stdin = open('2884_alam_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    H, M = map(int, input().split())
    if M < 45:
        M = 60 - (45 - M)
        if H == 0:
            H = 23
        else:
            H = H -1
    else:
        H = H
        M = M - 45
    print(H, M)