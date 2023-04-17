import sys
sys.stdin = open('17144_goodbye_dust_input.txt')


def dust(stack, time):
    global result
    cor = stack
    if time % 2 == 1:
        while cor:
            n, m, d = cor.pop()
            bit = 0
            if (n == 0 and m != 0) or (n == N-1 and m != 0):
                if temp_1[n][m-1] == -1:
                    temp_0[n][m] = 0
                    bit = 1
                else:
                    temp_1[n][m-1] += temp_0[n][m]
                    temp_0[n][m] = 0
                y, x = n, m-1
            elif (n == cleaner[0][0] and m != M-1) or (n == cleaner[1][0] and m != M-1):
                if temp_1[n][m+1] == -1:
                    temp_0[n][m] = 0
                    bit = 1
                else:
                    temp_1[n][m+1] += temp_0[n][m]
                    temp_0[n][m] = 0
                y, x = n, m + 1
            elif (m == 0 and 0 <= n < cleaner[0][0]) or (m == M-1 and cleaner[1][0] < n < N-1):
                if temp_1[n+1][m] == -1:
                    temp_0[n][m] = 0
                    bit = 1
                else:
                    temp_1[n+1][m] += temp_0[n][m]
                    temp_0[n][m] = 0
                y, x = n + 1, m
            elif (m == M-1 and 0 <= n <= cleaner[0][0]) or (m == 0 and cleaner[1][0] < n <= N-1):
                if temp_1[n-1][m] == -1:
                    temp_0[n][m] = 0
                    bit = 1
                else:
                    temp_1[n-1][m] += temp_0[n][m]
                    temp_0[n][m] = 0
                y, x = n - 1, m
            else:
                temp_1[n][m] += temp_0[n][m]
                temp_0[n][m] = 0
                y, x = n, m
            spread = d//5
            if spread == 0:
                continue
            count = 0
            for k in range(4):
                ny, nx = n+dy[k], m+dx[k]
                if 0 <= ny < N and 0 <= nx < M and temp_1[ny][nx] != -1:
                    if (ny == 0 and nx != 0) or (ny == N - 1 and nx != 0):
                        if temp_0[ny][nx-1] != -1:
                            temp_1[ny][nx - 1] += spread
                            count += 1
                    elif (ny == cleaner[0][0] and nx != M - 1) or (ny == cleaner[1][0] and nx != M - 1):
                        if temp_0[ny][nx+1] != -1:
                            temp_1[ny][nx + 1] += spread
                            count += 1
                    elif (nx == 0 and 0 <= ny < cleaner[0][0]) or (nx == M - 1 and cleaner[1][0] < ny < N - 1):
                        if temp_0[ny+1][nx] != -1:
                            temp_1[ny + 1][nx] += spread
                            count += 1
                    elif (nx == M - 1 and 0 <= ny <= cleaner[0][0]) or (nx == 0 and cleaner[1][0] < ny <= N - 1):
                        if temp_0[ny-1][nx] != -1:
                            temp_1[ny - 1][nx] += spread
                            count += 1
                    else:
                        temp_1[ny][nx] += spread
                        count += 1
            temp_1[y][x] -= spread*count

    if time % 2 == 0:
        while cor:
            n, m, d = cor.pop()
            bit = 0
            if (n == 0 and m != 0) or (n == N-1 and m != 0):
                if temp_0[n][m-1] == -1:
                    temp_1[n][m] = 0
                    bit = 1
                else:
                    temp_0[n][m-1] += temp_1[n][m]
                    temp_1[n][m] = 0
                y, x = n, m-1
            elif (n == cleaner[0][0] and m != M-1) or (n == cleaner[1][0] and m != M-1):
                if temp_0[n][m+1] == -1:
                    temp_1[n][m] = 0
                    bit = 1
                else:
                    temp_0[n][m+1] += temp_1[n][m]
                    temp_1[n][m] = 0
                y, x = n, m + 1
            elif (m == 0 and 0 <= n < cleaner[0][0]) or (m == M-1 and cleaner[1][0] <= n < N-1):
                if temp_0[n+1][m] == -1:
                    temp_1[n][m] = 0
                    bit = 1
                else:
                    temp_0[n+1][m] += temp_1[n][m]
                    temp_1[n][m] = 0
                y, x = n + 1, m
            elif (m == M-1 and 0 <= n <= cleaner[0][0]) or (m == 0 and cleaner[1][0] < n <= N-1):
                if temp_0[n-1][m] == -1:
                    temp_1[n][m] = 0
                    bit = 1
                else:
                    temp_0[n-1][m] += temp_1[n][m]
                    temp_1[n][m] = 0
                y, x = n - 1, m
            else:
                temp_0[n][m] += temp_1[n][m]
                temp_1[n][m] = 0
                y, x = n, m
            spread = d//5
            if spread == 0:
                continue
            count = 0
            for k in range(4):
                ny, nx = n+dy[k], m+dx[k]
                if 0 <= ny < N and 0 <= nx < M and temp_0[ny][nx] != -1:
                    if (ny == 0 and nx != 0) or (ny == N - 1 and nx != 0):
                        if temp_1[ny][nx-1] == -1:
                            continue
                        temp_0[ny][nx - 1] += spread
                        count += 1
                    elif (ny == cleaner[0][0] and nx != M - 1) or (ny == cleaner[1][0] and nx != M - 1):
                        if temp_1[ny][nx+1] == -1:
                            continue
                        temp_0[ny][nx + 1] += spread
                        count += 1
                    elif (nx == 0 and 0 <= ny < cleaner[0][0]) or (nx == M - 1 and cleaner[1][0] <= ny < N - 1):
                        if temp_1[ny+1][nx] == -1:
                            continue
                        temp_0[ny + 1][nx] += spread
                        count += 1
                    elif (nx == M - 1 and 0 <= ny <= cleaner[0][0]) or (nx == 0 and cleaner[1][0] < ny <= N - 1):
                        if temp_1[ny-1][nx] == -1:
                            continue
                        temp_0[ny - 1][nx] += spread
                        count += 1
                    else:
                        temp_0[ny][nx] += spread
                        count += 1
            temp_0[y][x] -= spread*count


def reset(time):
    global result
    result = 0
    if time % 2 == 1:
        for iy in range(N):
            for jx in range(M):
                if temp_1[iy][jx] > 0:
                    result += temp_1[iy][jx]
                    coordinate_even.append([iy, jx, temp_1[iy][jx]])

    if time % 2 == 0:
        for iy in range(N):
            for jx in range(M):
                if temp_0[iy][jx] > 0:
                    result += temp_0[iy][jx]
                    coordinate_odd.append([iy, jx, temp_0[iy][jx]])



dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


N, M, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
temp_0 = [[0]*M for _ in range(N)]
temp_1 = [[0]*M for _ in range(N)]

cleaner = []

coordinate_odd = []
coordinate_even = []

result = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            temp_0[i][j] = arr[i][j]
            coordinate_odd.append([i, j, arr[i][j]])
        if arr[i][j] == -1:
            temp_0[i][j] = -1
            temp_1[i][j] = -1
            cleaner.append([i, j])

for t in range(1, T+1):
    if t % 2 == 1:
        dust(coordinate_odd, t)
        reset(t)
    if t % 2 == 0:
        dust(coordinate_even, t)
        reset(t)

print('-----temp_0')
for i in temp_0:
    print(i)
print('-----temp_1')
for i in temp_1:
    print(i)

print(result)