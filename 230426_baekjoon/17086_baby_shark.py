import sys
sys.stdin = open('17086_baby_shark_input.txt')

dy = [0, 1, 1, 1, 0, -1, -1, -1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]


def check(q):
    q = q
    while q:
        n, m, s = q.pop(0)
        for k in range(8):
            ny, nx = n + dy[k], m + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = s
                    q.append([ny, nx, s+1])




N, M = map(int, input().split())

arr = [list(map(int, input().split()))]

visited = [[0]*M for _ in range(N)]

stack = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            check([i, j, 0])

print(visited)