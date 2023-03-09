import sys
sys.stdin = open('2480_three_dice_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    A, B, C = map(int, input().split())

    if A != B and A != C and B != C:
        print(max(A,B,C) * 100)

    if A == B and A != C and B != C:
        print(1000 + A * 100)

    if A != B and A != C and B == C:
        print(1000 + B * 100)

    if A != B and A == C and B != C:
        print(1000 + C * 100)

    if A == B == C :
        print(10000 + A * 1000)

