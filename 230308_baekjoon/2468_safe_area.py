import sys
sys.stdin = open('2468_safe_area_input.txt')
from collections import deque
input = sys.stdin.readline

def BFS(que):
    global max_count
    global count
    q = que
    while q:
        m, n = q.pop(0)
        for k in range(4):
            nx, ny = n + dx[k], m + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[ny][nx] != 1:
                    visited[ny][nx] = 1
                    q.append([ny, nx])
    count += 1
    if max_count < count:
        max_count = count




dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_count = 1

que = []

max_result = 0
for i in range(N):
    for j in range(N):
        if max_result < arr[i][j]:
            max_result = arr[i][j]

for p in range(1, max_result + 1):
    count = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if p >= arr[i][j]:
                visited[i][j] = 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 1:
                que.append([i, j])
                BFS(que)

print(max_count)