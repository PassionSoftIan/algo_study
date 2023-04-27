import sys
sys.stdin = open('1937_greedy_panda_input.txt')


def dfs(stack):
    global max_count, count
    stack = [stack]
    n, m = stack.pop()
    info[n][m] = 1
    for k in range(4):
        ny, nx = n + dy[k], m + dx[k]
        if 0 <= ny < N and 0 <= nx < N:
            if visited[ny][nx] == 0:
                if arr[ny][nx] > arr[n][m]:
                    visited[ny][nx] = 1
                    count += 1
                    dfs([ny, nx])
                    if max_count <= count:
                        max_count = count
                    count -= 1
                    visited[ny][nx] = 0


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
info = [[0] * N for _ in range(N)]

max_count = 0

count = 1

for i in range(N):
    for j in range(N):
        if info[i][j] == 0:
            visited[i][j] = 1
            dfs([i, j])
            visited[i][j] = 0
for i in info:
    print(i)
print(max_count)