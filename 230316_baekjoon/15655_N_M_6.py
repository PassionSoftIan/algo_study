import sys
sys.stdin = open('15655_N_M_6_input.txt')

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
result = []
def backtracking(depth, s):
    if depth == M:
        print(*result)

    for i in range(s, N):
        if num[i] not in result:
            result.append(num[i])
            backtracking(depth+1, i)
            result.pop()

backtracking(0, 0)