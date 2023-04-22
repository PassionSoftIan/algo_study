import sys
sys.stdin = open('1719_post_input.txt')
# input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1e9)
arr = [[INF]*(N+1) for _ in range(N+1)]
visited = [[0]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    arr[i][i] = 0

for i in range(1, N+1):
    visited[i][i] = '-'

for mc in range(M):
    start, end, time = map(int, input().split())
    if arr[start][end] > time:
        arr[start][end] = time
        visited[start][end] = end

    if arr[end][start] > time:
        arr[end][start] = time
        visited[end][start] = start

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
                visited[i][j] = visited[i][k]

for i in visited[1:]:
    print(*i[1:])