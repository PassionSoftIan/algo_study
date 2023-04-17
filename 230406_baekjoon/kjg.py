import sys
sys.stdin = open('17144_goodbye_dust_input.txt')

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dust(coord, second):
    global result
    if second % 2 == 0:
        stack = coord
        for ci in range(len(stack)):
            final_arr[stack[ci][0]][stack[ci][1]] = arr[stack[ci][0]][stack[ci][1]]
        while stack:
            bit = 0
            n, m = stack.pop()
            visited[n][m] = final_arr[n][m]
            if n == 0 or n == cleaner[0][0] or n == cleaner[1][0] or n == R-1:
                if info_d[n][m] == 0:
                    dirty.append([n, m])
                    info_d[n][m] = 1
                    bit = 1
            if (m == 0 or m == C-1) and (0 < n < cleaner[0][0] or cleaner[1][0] < n < R-1):
                if info_d[n][m] == 0:
                    dirty.append([n, m])
                    info_d[n][m] = 1
                    bit = 1
            if info_c[n][m] == 0 and bit == 0:
                coordinate_odd.append([n, m])
                info_c[n][m] = 1
            for k in range(4):
                ny, nx = n + dy[k], m + dx[k]
                if 0 <= ny < R and 0 <= nx < C:
                    if (ny != cleaner[0][0] and nx != cleaner[0][1]) or (ny != cleaner[1][0] and nx != cleaner[1][1]):
                        final_arr[ny][nx] += arr[n][m] // 5
                        final_arr[n][m] -= arr[n][m] // 5
                        visited[ny][nx] += arr[n][m] // 5
                        visited[n][m] -= arr[n][m] // 5
                        if ny == 0 or ny == cleaner[0][0] or ny == cleaner[1][0] or ny == R - 1:
                            if info_d[ny][nx] == 0:
                                dirty.append([ny, nx])
                                info_d[ny][nx] = 1
                                continue
                        if (nx == 0 or nx == C - 1) and (0 < ny < cleaner[0][0] or cleaner[1][0] < ny < R - 1):
                            if info_d[ny][nx] == 0:
                                dirty.append([ny, nx])
                                info_d[ny][nx] = 1
                                continue
                        if info_c[ny][nx] == 0:
                            coordinate_odd.append([ny, nx])
            arr[n][m] = 0

    if second % 2 == 1:
        stack = coord
        for ci in range(len(stack)):
            arr[stack[ci][0]][stack[ci][1]] = final_arr[stack[ci][0]][stack[ci][1]]
        while stack:
            bit = 0
            n, m = stack.pop()
            visited[n][m] = arr[n][m]
            if n == 0 or n == cleaner[0][0] or n == cleaner[1][0] or n == R - 1:
                if info_d[n][m] == 0:
                    dirty.append([n, m])
                    info_d[n][m] = 1
                    bit = 1
            if (m == 0 or m == C - 1) and (0 < n < cleaner[0][0] or cleaner[1][0] < n < R - 1):
                if info_d[n][m] == 0:
                    dirty.append([n, m])
                    info_d[n][m] = 1
                    bit = 1
            if info_c[n][m] == 0 and bit == 0:
                coordinate_even.append([n, m])
                info_c[n][m] = 1
            for k in range(4):
                ny, nx = n + dy[k], m + dx[k]
                if 0 <= ny < R and 0 <= nx < C:
                    if (ny != cleaner[0][0] and nx != cleaner[0][1]) or (
                            ny != cleaner[1][0] and nx != cleaner[1][1]):
                        arr[ny][nx] += final_arr[n][m] // 5
                        arr[n][m] -= final_arr[n][m] // 5
                        visited[ny][nx] += final_arr[n][m] // 5
                        visited[n][m] -= final_arr[n][m] // 5
                        if ny == 0 or ny == cleaner[0][0] or ny == cleaner[1][0] or ny == R - 1:
                            if info_d[ny][nx] == 0:
                                dirty.append([ny, nx])
                                info_d[ny][nx] = 1
                                continue
                        if (nx == 0 or nx == C - 1) and (0 < ny < cleaner[0][0] or cleaner[1][0] < ny < R - 1):
                            if info_d[ny][nx] == 0:
                                dirty.append([ny, nx])
                                info_d[ny][nx] = 1
                                continue
                        if info_c[ny][nx] == 0:
                            coordinate_even.append([ny, nx])
            final_arr[n][m] = 0


def purify_arr(drt):
    global result
    dirty_p = drt
    for pi in range(len(dirty_p)):
        final_arr[dirty_p[pi][0]][dirty_p[pi][1]] = 0
    while dirty_p:
        py, px = dirty_p.pop()
        if py+1 == cleaner[0][0] and px == 0:
            result -= visited[py][px]
            continue
        if py-1 == cleaner[1][0] and px == 0:
            result -= visited[py][px]
            continue
        if py == 0 or py == R-1:
            if py == 0 and px == 0:
                final_arr[py+1][px] = visited[py][px]
                coordinate_odd.append([py+1, px])
                continue
            elif py == R-1 and px == 0:
                final_arr[py-1][px] = visited[py][px]
                coordinate_odd.append([py-1, px])
                continue
            else:
                final_arr[py][px-1] = visited[py][px]
                coordinate_odd.append([py, px-1])
                continue
        if py == cleaner[0][0] or py == cleaner[1][0]:
            if py == cleaner[0][0] and px == C-1:
                final_arr[py-1][px] = visited[py][px]
                coordinate_odd.append([py-1, px])
                continue
            elif py == cleaner[1][0] and px == C-1:
                final_arr[py+1][px] = visited[py][px]
                coordinate_odd.append([py+1, px])
                continue
            else:
                final_arr[py][px+1] = visited[py][px]
                coordinate_odd.append([py, px+1])
                continue
        if px == 0:
            if py < cleaner[0][0]:
                final_arr[py+1][px] = visited[py][px]
                coordinate_odd.append([py+1, px])
                continue
            if cleaner[1][0] < py:
                final_arr[py-1][px] = visited[py][px]
                coordinate_odd.append([py-1, px])
                continue
        if px == C-1:
            if 0 < py < cleaner[0][0]:
                final_arr[py-1][px] = visited[py][px]
                coordinate_odd.append([py-1, px])
                continue
            if cleaner[1][0] < py < R-1:
                final_arr[py+1][px] = visited[py][px]
                coordinate_odd.append([py+1, px])
                continue


def purify_final(drt):
    global result
    dirty_p = drt
    for pi in range(len(dirty_p)):
        arr[dirty_p[pi][0]][dirty_p[pi][1]] = 0
    while dirty_p:
        py, px = dirty_p.pop()
        if py+1 == cleaner[0][0] and px == 0:
            result -= visited[py][px]
            continue
        if py-1 == cleaner[1][0] and px == 0:
            result -= visited[py][px]
            continue
        if py == 0 or py == R-1:
            if py == 0 and px == 0:
                arr[py+1][px] = visited[py][px]
                coordinate_even.append([py, px])
                continue
            elif py == R-1 and px == 0:
                arr[py-1][px] = visited[py][px]
                coordinate_even.append([py, px])
                continue
            else:
                arr[py][px-1] = visited[py][px]
                coordinate_even.append([py, px])
                continue
        if py == cleaner[0][0] or py == cleaner[1][0]:
            if py == cleaner[0][0] and px == C-1:
                arr[py-1][px] = visited[py][px]
                coordinate_even.append([py, px])
                continue
            elif py == cleaner[1][0] and px == C-1:
                arr[py+1][px] = visited[py][px]
                coordinate_even.append([py, px])
                continue
            else:
                arr[py][px+1] = visited[py][px]
                coordinate_even.append([py, px])
                continue
        if px == 0:
            if py < cleaner[0][0]:
                arr[py+1][px] = visited[py][px]
                coordinate_even.append([py, px])
                continue
            if cleaner[1][0] < py:
                arr[py-1][px] = visited[py][px]
                coordinate_even.append([py, px])
                continue
        if px == C-1:
            if 0 < py < cleaner[0][0]:
                arr[py-1][px] = visited[py][px]
                coordinate_even.append([py, px])
                continue
            if cleaner[1][0] < py < R-1:
                arr[py+1][px] = visited[py][px]
                coordinate_even.append([py, px])
                continue


R, C, T = map(int, input().split())  # R세로, C 가로, T 시간
arr = [list(map(int, input().split())) for _ in range(R)]
final_arr = [[0]*C for _ in range(R)]
info_c = [[0] * C for _ in range(R)]
visited = [[0] * C for _ in range(R)]

coordinate_odd = []
coordinate_even = []

dirty = []

cleaner = []

result = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            result += arr[i][j]
            coordinate_even.append([i, j])
        if arr[i][j] == -1:
            final_arr[i][j] += arr[i][j]
            cleaner.append([i, j])

for i in range(T):
    if i % 2 == 0:
        visited = [[0] * C for _ in range(R)]
        info_d = [[0] * C for _ in range(R)]
        info_c = [[0] * C for _ in range(R)]
        dust(coordinate_even, i)
        purify_arr(dirty)
        print(f'{i} --arr')
        for z in arr:
            print(z)

    if i % 2 == 1:
        visited = [[0] * C for _ in range(R)]
        info_d = [[0] * C for _ in range(R)]
        info_c = [[0] * C for _ in range(R)]
        dust(coordinate_odd, i)
        purify_final(dirty)
        print(f'{i} --final')
        for z in final_arr:
            print(z)




print(result)