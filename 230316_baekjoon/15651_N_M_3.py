import sys
sys.stdin = open('15651_N_M_3_input.txt')

N, M = map(int, input().split())

num = sorted(list(range(1, N+1)))

result = []
def backtracking(depth):
    if depth == M:
        print(*result)
        return
    for i in range(N):
        result.append(num[i])
        backtracking(depth+1)
        result.pop()
backtracking(0)

