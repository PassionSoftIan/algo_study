import sys
sys.stdin = open('17144_goodbye_dust_input.txt')


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def spread(dust, second):
    dirty = dust
    info = [[0]*C for _ in range(R)]
    if second % 2 == 0:
        while dirty:
            n, m = dirty.pop()
            for k in range(4):
                ny, nx = n + dy[k], m + dx[k]
                if 0 <= ny < R and 0 <= nx < C:
                    if arr[ny][nx] != -1:
                        if ny == 0 or ny == R-1 or ny == cleaner[0][0] or ny == cleaner[1][0]\
                                or nx == 0 or nx == C-1:
                            if info[ny][nx] == 0:
                                visited[ny][nx] += arr[ny][nx]
                                info[ny][nx] = 1
                            visited[ny][nx] += arr[n][m]//5
                            arr[n][m] -= arr[n][m]//5
                        else:
                            if info[ny][nx] == 0:
                                visited[ny][nx] += arr[ny][nx]
                                info[ny][nx] = 1
                            arr[ny][nx] += arr[n][m]//5
                            arr[n][m] -= arr[n][m]//5


    else:
        pass


# def check(chk, second):
#     full = chk
#     if second % 2 == 0:
#         while full:
#             fy, fx = full.pop
#             arr_2[fy][fx]



R, C, T = map(int, input().split())  # R세로, C 가로, T 시간
arr = [list(map(int, input().split())) for _ in range(R)]
arr_2 = [[0]*C for _ in range(R)]

coordinate_spread = []
coordinate_check = []
cleaner = []

for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            cleaner.append([i, j])

for time in range(T):
    if time % 2 == 0:
        visited = [[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if arr[i][j] >= 5:
                    coordinate_spread.append([i, j])
                    continue
                if arr[i][j] > 0:
                    coordinate_check.append([i, j])
        spread(coordinate_spread, time)
        # check(coordinate_check, time)

for i in visited:
    print(i)



# print(result)