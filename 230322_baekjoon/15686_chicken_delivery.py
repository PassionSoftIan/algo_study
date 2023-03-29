import sys
sys.stdin = open('15686_chicken_delivery_input.txt')
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS(st):
    lst = []
    visited = [[0] * N for _ in range(N)]
    q = deque(st)
    while q:
        n, m = q.popleft()
        for k in range(4):
            nx, ny = m + dx[k], n + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[ny][nx] != 1 and visited[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = 1
                if arr[ny][nx] == 1 and visited[ny][nx] == 0:
                    lst.append(abs(i - ny) + abs(j - nx))
                    q.append([ny, nx])
                    visited[ny][nx] = 1
    return lst

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

result_lst = []

start = deque()
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            start.append([i, j])
            result_lst.append(BFS(start))
            start.popleft()

print(result_lst)
min_result = []

for i in range(len(result_lst)):
    print(sum(result_lst[i]))