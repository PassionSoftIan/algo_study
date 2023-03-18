import sys
sys.stdin = open('15663_N_M_9_input.txt')

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0] * N
result = []

def backtracking(depth):
    if depth == M:
        print(*result)
        return

    prev = 0
    for i in range(N):
        if visited[i] == 0 and prev != num[i]:
            result.append(num[i])
            visited[i] = 1
            prev = num[i]
            backtracking(depth+1)
            visited[i] = 0
            result.pop()

backtracking(0)