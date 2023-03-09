import sys
sys.stdin = open('10026_red_green_weakness_input.txt')

def BFS(q):
    queue = q
    while queue:
        m, n = queue.pop(0)
        for k in range(4):
            nx, ny = n + dx[k], m + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[ny][nx] == arr[i][j] and visited[ny][nx] == 0:
                    if ny == i and nx == j:
                        continue
                    else:
                        if arr[i][j] == 'B':
                            visited[ny][nx] = 2
                            queue.append([ny, nx])
                        else:
                            visited[ny][nx] = 1
                            queue.append([ny, nx])

def BFS_weak(q):
    queue = q
    while queue:
        m, n = queue.pop(0)
        for k in range(4):
            nx, ny = n + dx[k], m + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[ny][nx] == visited[i][j] and visited2[ny][nx] == 0:
                    if ny == i and nx == j:
                        continue
                    else:
                        visited2[ny][nx] = 1
                        queue.append([ny, nx])


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())

arr = [list(input().strip()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]


q = []
count = 0
count_weak = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R' and visited[i][j] == 0:
            count += 1
            visited[i][j] = 1
            q.append([i, j])
            BFS(q)
        if arr[i][j] == 'G' and visited[i][j] == 0:
            count += 1
            visited[i][j] = 1
            q.append([i, j])
            BFS(q)
        if arr[i][j] == 'B' and visited[i][j] == 0:
            count += 1
            visited[i][j] = 2
            q.append([i, j])
            BFS(q)

for i in range(N):
    for j in range(N):
        if (visited[i][j] == 1 or visited[i][j] == 2) and visited2[i][j] == 0:
            visited2[i][j] = 1
            count_weak += 1
            q.append([i, j])
            BFS_weak(q)
        # if visited == 1

print(count, count_weak, visited)