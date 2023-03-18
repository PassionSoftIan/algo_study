import sys
sys.stdin = open('15649_N_M_1_input.txt')

N, M = map(int, input().split())

num = list(range(1, N+1))

result = []

def backtracking(depth):
    if depth == M:
        print(*result)
        return
    for i in range(N):
        if num[i] not in result:
            result.append(num[i])
            backtracking(depth+1)
            result.pop()

backtracking(0)