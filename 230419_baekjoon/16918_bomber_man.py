import sys
sys.stdin = open('16918_bomber_man_input.txt')

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


N, M, T = map(int, input().split())

arr = [list(map(str, input())) for _ in range(N)]

bomb = []

launch = []

count = 1

if T == 0 or T == 1:
    for i in arr:
        print(*i, sep='')
    exit()

while True:
    if count == T+1:
        for i in arr:
            print(*i, sep='')
        break

    if count % 2 == 0:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 'O':
                    bomb.append([i, j])
                if arr[i][j] == '.':
                    launch.append([i, j])
        while launch:
            n, m = launch.pop()
            arr[n][m] = 'O'

    if count % 2 == 1:
        while bomb:
            n, m = bomb.pop()
            arr[n][m] = '.'
            for k in range(4):
                ny, nx = n + dy[k], m + dx[k]
                if 0 <= ny < N and 0 <= nx < M:
                    arr[ny][nx] = '.'
    count += 1