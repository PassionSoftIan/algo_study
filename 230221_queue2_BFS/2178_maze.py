import sys
sys.stdin = open('2178_maze_input.txt')

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * (M) for _ in range(N)]
# print(visited)
start = [[0, 0]]
visited[0][0] = 1
# print(i,j)
while start:
    i, j = start.pop(0)
    for k in range(4):
        nx, ny = j + dx[k], i + dy[k]
        if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0 and arr[ny][nx] == 1:
            if arr[ny][nx] == 1:
                start.append([ny, nx])
                visited[ny][nx] = visited[i][j] + 1
# for i in visited:
#     print(i)
print(visited[N-1][M-1])