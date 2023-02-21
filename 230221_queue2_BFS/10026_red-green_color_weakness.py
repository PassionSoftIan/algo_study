import sys
sys.stdin = open('10026_red_green_color_weakness.txt')

N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = [[0,0]]
visited[0][0] = 1
result = 0
check = True
while check:
    # i, j = q.pop(0)
    # for k in range(4):
    #     nx, ny = j + dx[k], i + dy[k]
    #     if 0 <= nx < N and 0 <= ny < N:
    #         if arr[ny][nx] == arr[i][j] and visited[ny][nx] == 0:
    #             q.append([ny, nx])
    #             visited[ny][nx] += 1
    #         if len(q) == 1 and arr[ny][nx] != arr[i][j] and visited[ny][nx] == 0:
    #             q.append([ny, nx])
    #             visited[ny][nx] += 1
    #             result += 1
    #         if not q:
    #             break
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'G':
                arr[i][j] = 'R'
    for k in range(4):
        nx, ny = j + dx[k], i + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[ny][nx] == arr[i][j] and visited[ny][nx] == 0:
                q.append([ny, nx])
                visited[ny][nx] += 1
            if len(q) == 1 and arr[ny][nx] != arr[i][j] and visited[ny][nx] == 0:
                q.append([ny, nx])
                visited[ny][nx] += 1
                result += 1
            if not q:
                check = False
for i in arr:
    print(i)
for i in visited:
    print(i)
print(result)


# q_red = []
# q_blue = []
# q_green = []
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 'R':
#             q_red.append([i, j])
#             break
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 'B':
#             q_red.append([i, j])
#             break
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 'G':
#             q_red.append([i, j])
#             break
# visited_red[i][j]
# visited_blue[i][j]
# visited_green[i][j]
# result = 0
# while q_red:
#     i, j = q_red.pop()
#     for k in range(4):
#         nx, ny = j + dx[k], i + dy[k]
#         if 0 <= nx < N and 0 <= ny < N:
#             if arr[ny][nx] == 'R' and visited_red[ny][nx] == 0:
#                 q_red.append([ny, nx])
#                 visited_red[ny][nx] += 1
# else:
#     result += 1
# while q_blue:
#     i, j = q_blue.pop()
#     for k in range(4):
#         nx, ny = j + dx[k], i + dy[k]
#         if 0 <= nx < N and 0 <= ny < N:
#             if arr[ny][nx] == 'B' and visited_blue[ny][nx] == 0:
#                 q_blue.append([ny, nx])
#                 visited_blue[ny][nx] += 1
# else:
#     result += 1
# while q_green:
#     i, j = q_green.pop()
#     for k in range(4):
#         nx, ny = j + dx[k], i + dy[k]
#         if 0 <= nx < N and 0 <= ny < N:
#             if arr[ny][nx] == 'G' and visited_green[ny][nx] == 0:
#                 q_green.append([ny, nx])
#                 visited_green[ny][nx] += 1
# else:
#     result += 1
#
# print(visited_red)
# print(visited_blue)
# print(visited_green)
# print(result)