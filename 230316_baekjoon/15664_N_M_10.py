import sys
sys.stdin = open('15664_N_M_10_input.txt')

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0] * N
result = []

def backtracking(depth, s):
    if depth == M:
        print(*result)
        return

    prev = 0
    for i in range(s, N):
        if visited[i] == 0 and prev != num[i]:
            result.append(num[i])
            visited[i] = 1
            prev = num[i]
            backtracking(depth+1, i)
            visited[i] = 0
            result.pop()

backtracking(0, 0)