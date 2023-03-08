import sys
sys.stdin = open('230307_food_trash_input.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(K)]
arr = [[0]*(M+1) for _ in range(N+1)]
visited = [[0] * (M+1) for _ in range(N+1)]

for i in mat:
    m, n = i
    arr[m][n] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
stack = []

max_count = 0
for i in range(N + 1):
    for j in range(M + 1):
        count = 1
        if arr[i][j] == 1:
            stack.append([i, j])
            while stack:
                m, n = stack.pop()
                visited[m][n] = 1
                for k in range(4):
                    nx, ny = n + dx[k], m + dy[k]
                    if 0 <= nx < M+1 and 0 <= ny < N+1:
                        if arr[ny][nx] == 1 and visited[ny][nx] == 0:
                            stack.append([ny,nx])
                            visited[ny][nx] = 1
                            count += 1
            if count > max_count:
                max_count = count
print(max_count)