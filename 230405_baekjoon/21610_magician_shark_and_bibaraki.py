import sys
sys.stdin = open('21610_magician_shark_and_bibaraki_input.txt')

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]


def rain(stk, info):
    stack = stk
    plus = []
    information = [info]
    d, t = information.pop()
    while stack:
        n, m = stack.pop()
        ny = n + t*dy[d-1]
        nx = m + t*dx[d-1]
        arr[ny % N][nx % N] += 1
        visited[ny % N][nx % N] = 1
        plus.append([ny % N, nx % N])
    check(plus)


def check(pls):
    pl = pls
    while pl:
        py, px = pl.pop()
        for cc in range(1, 8, 2):
            cy, cx = py + dy[cc], px + dx[cc]
            if 0 <= cy < N and 0 <= cx < N:
                if arr[cy][cx] > 0:
                    arr[py][px] += 1


def replay():
    for ic in range(N):
        for jc in range(N):
            if arr[ic][jc] >= 2 and visited[ic][jc] == 0:
                arr[ic][jc] -= 2
                coordinate.append([ic, jc])


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

direction_info = [list(map(int, input().split())) for _ in range(M)]

coordinate = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

for mc in range(M):
    visited = [[0]*N for _ in range(N)]
    rain(coordinate, direction_info[mc])
    replay()

result = 0
for i in range(N):
    for j in range(N):
        result += arr[i][j]


print(result)