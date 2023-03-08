import sys
sys.stdin = open('2525_oven_timer_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    A, B = map(int, input().split())
    C = int(input())

    if C + B < 60:
        A = A
        B = C + B
    else:
        A = (A + (C+B)//60) % 24
        B = (C+B) % 60


    print(A, B)