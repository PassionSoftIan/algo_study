import sys
sys.stdin = open('17086_baby_shark_input.txt')
from collections import deque


dy = [0, 1, 1, 1, 0, -1, -1, -1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]


def check(q):
    visited = [[0]*M for _ in range(N)]
    count = 0
    q = deque([q])
    while q:
        if count == N*M-1:
            return
        n, m, s = q.popleft()
        for k in range(8):
            ny, nx = n + dy[k], m + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == 0 and arr[ny][nx] == 0:
                    visited[ny][nx] = 1
                    count += 1
                    q.append([ny, nx, s+1])
                    if info[ny][nx] > s:
                        info[ny][nx] = s
                if arr[ny][nx] == 1 and info[ny][nx] == 5001:
                    count += 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

info = [[5001]*M for _ in range(N)]

bit = 0

result = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            info[i][j] = 1
            check([i, j, 1])
            bit = 1

if bit == 0:
    print(0)
    exit()

for i in info:
    result = max(result, max(i))

for i in info:
    print(i)

print(result)