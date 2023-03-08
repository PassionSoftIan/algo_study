import sys
sys.stdin = open('2480_three_dice_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    A, B, C = map(int, input().split())
    if (A == B and A == C) or (B == A and B == C) or (C == A and C == B):
        print(10000 + A * 1000)
        continue
    if (A == B or A == C) or (B == C or B == A) or (C == A or C == B):
        print(1000 + A * 100)
        continue
    if A != B and A != C and B != C:
        print(max(A, B, C) * 100)
        continue