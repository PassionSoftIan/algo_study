import sys
sys.stdin = open('10026_red_green_weakness_input.txt')

def BFS(q):

    queue = q
    while queue:
        m, n = queue.pop(0)
        for k in range(4):
            nx, ny = n + dx[k], m + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[ny][nx] == arr[i][j] and arr[ny][nx] != 'v':
                    if ny == i and nx == j:
                        continue
                    else:
                        arr[ny][nx] = 'v'
                        queue.append([ny, nx])

def BFS_weak(q):

    queue = q
    while queue:
        m, n = queue.pop(0)
        for k in range(4):
            nx, ny = n + dx[k], m + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[i][j] == 'R' or arr[i][j] == 'G':
                    if arr[ny][nx] == 'R' or arr[ny][nx] == 'G' and arr[ny][nx] != 'v':
                        if ny == i and nx == j:
                            continue
                        else:
                            arr[ny][nx] = 'v'
                            queue.append([ny, nx])
                else:
                    if arr[ny][nx] != 'v' and arr[ny][nx] == arr[i][j]:
                        if ny == i and nx == j:
                            continue
                    else:
                        arr[ny][nx] = 'v'
                        queue.append([ny, nx])



dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())

arr = [list(input().strip()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

q = []
count = 0
count_weak = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R' and visited[i][j] == 0:
            count += 1
            count_weak += 1
            visited[i][j] = 1
            q.append([i, j])
            BFS(q)
            BFS_weak(q)
        if arr[i][j] == 'G' and visited[i][j] == 0:
            count += 1
            count_weak += 1
            visited[i][j] = 1
            q.append([i, j])
            BFS(q)
            BFS_weak(q)
        if arr[i][j] == 'B' and visited[i][j] == 0:
            count += 1
            count_weak += 1
            visited[i][j] = 1
            q.append([i, j])
            BFS(q)
            BFS_weak(q)

print(count)
print(count_weak)