import sys
sys.stdin = open('16918_bomber_man_input.txt')


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


N, M, T = map(int, input().split())

arr = [list(map(str, input())) for _ in range(N)]

coordinate = []

while True:
    if T == 1:
        for i in arr:
            print(*i, sep='')
        break
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '0':
                coordinate.append([i, j])
    while coordinate:
        n, m = coordinate.pop()
        for k in range(4):
            ny, nx = n + dy[k], m + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                arr[ny][nx] = '.'

# for i in arr:
#     print(*i, sep='')