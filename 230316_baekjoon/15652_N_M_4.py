import sys
sys.stdin = open('15652_N_M_4_input.txt')

N, M = map(int, input().split())
num = sorted(list(range(1, N+1)))

result = []
def backtracking(depth, s):
    if depth == M:
        print(*result)
        return
    for i in range(s, N):
        result.append(num[i])
        backtracking(depth+1, i)
        result.pop()
backtracking(0, 0)