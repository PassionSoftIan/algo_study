import sys
sys.stdin = open('17144_goodbye_dust_input.txt')


def dust(crd):
    coordination = crd
    while coordination:
        n, m, d = coordination.pop()
        visited[n][m] += d
        if info[n][m] == 0:
            info[n][m] = 1
            purify.append([n, m])
        spread = d//5
        if spread == 0:
            continue
        count = 0
        for k in range(4):
            ny, nx = n + dy[k], m + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] != -1:
                    visited[ny][nx] += spread
                    count += 1
                    if info[ny][nx] == 0:
                        info[ny][nx] = 1
                        purify.append([ny, nx])
        visited[n][m] -= (spread*count)
    purifying(visited, purify)


def purifying(visit, need_purify):
    global result
    need_purify = need_purify
    while need_purify:
        py, px = need_purify.pop()
        if px != 0 and (py == 0 or py == N-1):
            if visited[py][px-1] != -1:
                coordinate.append([py, px-1, visit[py][px]])
                visit[py][px] = 0
            else:
                result -= visit[py][px]
                visit[py][px] = 0
        elif px != M-1 and (py == cleaner[0][0] or py == cleaner[1][0]):
            if visited[py][px+1] != -1:
                coordinate.append([py, px+1, visit[py][px]])
                visit[py][px] = 0
            else:
                result -= visit[py][px]
        elif (px == 0 and 0 <= py < cleaner[0][0]) or (px == M-1 and cleaner[1][0] <= py <= N-1):
            if visited[py+1][px] != -1:
                coordinate.append([py+1, px, visit[py][px]])
                visit[py][px] = 0
            else:
                result -= visit[py][px]
                visit[py][px] = 0
        elif (px == M-1 and 0 <= py <= cleaner[0][0]) or (px == 0 and cleaner[1][0] < py <= N-1):
            if visited[py-1][px] != -1:
                coordinate.append([py-1, px, visit[py][px]])
                visit[py][px] = 0
            else:
                result -= visit[py][px]
                visit[py][px] = 0
        else:
            coordinate.append([py, px, visit[py][px]])
            visit[py][px] = 0


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


N, M, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

coordinate = []

purify = []

cleaner = []

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            result += arr[i][j]
            coordinate.append([i, j, arr[i][j]])
        if arr[i][j] == -1:
            cleaner.append([i, j])

visited = [[0] * M for _ in range(N)]
visited[cleaner[0][0]][cleaner[0][1]] = -1
visited[cleaner[1][0]][cleaner[1][1]] = -1

for t in range(T):
    info = [[0] * M for _ in range(N)]
    dust(coordinate)

print(result)

# def dust(crd, time):
#     coordination = crd
#     time = time
#     if time % 2 == 0:
#         while coordination:
#             n, m, d = coordination.pop()
#             visited[n][m] += d
#             temp_0[n][m] = 0
#             if info[n][m] == 0:
#                 info[n][m] = 1
#                 purify.append([n, m])
#             spread = d//5
#             if spread == 0:
#                 continue
#             count = 0
#             for k in range(4):
#                 ny, nx = n + dy[k], m + dx[k]
#                 if 0 <= ny < N and 0 <= nx < M:
#                     if visited[ny][nx] != -1:
#                         visited[ny][nx] += spread
#                         count += 1
#                         if info[ny][nx] == 0:
#                             info[ny][nx] = 1
#                             purify.append([ny, nx])
#             visited[n][m] -= (spread*count)
#         purifying(visited, purify, time)
#     else:
#         while coordination:
#             n, m, d = coordination.pop()
#             visited[n][m] += d
#             temp_1[n][m] = 0
#             if info[n][m] == 0:
#                 info[n][m] = 1
#                 purify.append([n, m])
#             spread = d // 5
#             if spread == 0:
#                 continue
#             count = 0
#             for k in range(4):
#                 ny, nx = n + dy[k], m + dx[k]
#                 if 0 <= ny < N and 0 <= nx < M:
#                     if visited[ny][nx] != -1:
#                         visited[ny][nx] += spread
#                         count += 1
#                         if info[ny][nx] == 0:
#                             info[ny][nx] = 1
#                             purify.append([ny, nx])
#             visited[n][m] -= (spread * count)
#         purifying(visited, purify, time)
#
#
# def purifying(visit, need_purify, time):
#     global result
#     time = time
#     need_purify = need_purify
#     if time % 2 == 0:
#         while need_purify:
#             py, px = need_purify.pop()
#             if px != 0 and (py == 0 or py == N-1):
#                 if temp_1[py][px-1] != -1:
#                     temp_1[py][px-1] = visit[py][px]
#                     coordinate.append([py, px-1, visit[py][px]])
#                 else:
#                     result -= visit[py][px]
#             elif px != M-1 and (py == cleaner[0][0] or py == cleaner[1][0]):
#                 if temp_1[py][px+1] != -1:
#                     temp_1[py][px+1] = visit[py][px]
#                     coordinate.append([py, px+1, visit[py][px]])
#                 else:
#                     result -= visit[py][px]
#             elif (px == 0 and 0 <= py < cleaner[0][0]) or (px == M-1 and cleaner[1][0] <= py <= N-1):
#                 if temp_1[py+1][px] != -1:
#                     temp_1[py+1][px] = visit[py][px]
#                     coordinate.append([py+1, px, visit[py][px]])
#                 else:
#                     result -= visit[py][px]
#             elif (px == M-1 and 0 <= py <= cleaner[0][0]) or (px == 0 and cleaner[1][0] < py <= N-1):
#                 if temp_1[py-1][px] != -1:
#                     temp_1[py-1][px] = visit[py][px]
#                     coordinate.append([py-1, px, visit[py][px]])
#                 else:
#                     result -= visit[py][px]
#             else:
#                 temp_1[py][px] = visit[py][px]
#                 coordinate.append([py, px, visit[py][px]])
#     else:
#         while need_purify:
#             py, px = need_purify.pop()
#             if px != 0 and (py == 0 or py == N-1):
#                 if temp_0[py][px-1] != -1:
#                     temp_0[py][px-1] = visit[py][px]
#                     coordinate.append([py, px-1, visit[py][px]])
#                 else:
#                     result -= visit[py][px]
#             elif px != M-1 and (py == cleaner[0][0] or py == cleaner[1][0]):
#                 if temp_0[py][px+1] != -1:
#                     temp_0[py][px+1] = visit[py][px]
#                     coordinate.append([py, px+1, visit[py][px]])
#                 else:
#                     result -= visit[py][px]
#             elif (px == 0 and 0 <= py < cleaner[0][0]) or (px == M-1 and cleaner[1][0] <= py <= N-1):
#                 if temp_0[py+1][px] != -1:
#                     temp_0[py+1][px] = visit[py][px]
#                     coordinate.append([py+1, px, visit[py][px]])
#                 else:
#                     result -= visit[py][px]
#             elif (px == M-1 and 0 <= py <= cleaner[0][0]) or (px == 0 and cleaner[1][0] < py <= N-1):
#                 if temp_0[py-1][px] != -1:
#                     temp_0[py-1][px] = visit[py][px]
#                     coordinate.append([py-1, px, visit[py][px]])
#                 else:
#                     result -= visit[py][px]
#             else:
#                 temp_0[py][px] = visit[py][px]
#                 coordinate.append([py, px, visit[py][px]])
#
#
# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]
#
#
# N, M, T = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# temp_0 = [[0]*M for _ in range(N)]
# temp_1 = [[0]*M for _ in range(N)]
#
# coordinate = []
#
# purify = []
#
# cleaner = []
#
# result = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] > 0:
#             temp_0[i][j] = arr[i][j]
#             result += temp_0[i][j]
#             coordinate.append([i, j, arr[i][j]])
#         if arr[i][j] == -1:
#             temp_0[i][j] = -1
#             temp_1[i][j] = -1
#             cleaner.append([i, j])
#
#
# for t in range(T):
#     visited = [[0] * M for _ in range(N)]
#     info = [[0] * M for _ in range(N)]
#     visited[cleaner[0][0]][cleaner[0][1]] = -1
#     visited[cleaner[1][0]][cleaner[1][1]] = -1
#     if t % 2 == 0:
#         dust(coordinate, t)
#     else:
#         dust(coordinate, t)
# print(result)
# print('---temp_0')
# for i in temp_0:
#     print(i)
#
# print('---temp_1')
# for i in temp_1:
#     print(i)