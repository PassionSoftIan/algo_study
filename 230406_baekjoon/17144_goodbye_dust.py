import sys
sys.stdin = open('17144_goodbye_dust_input.txt')
# 148

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dust(coord):
    global result
    stack = coord
    while stack:
        n, m = stack.pop()
        for k in range(4):
            ny, nx = n + dy[k], m + dx[k]
            if 0 <= ny < R and 0 <= nx < C:
                if arr[ny][nx] >= 0:
                    final_arr[ny][nx] += arr[n][m]//5
                    result += arr[n][m]//5
                    final_arr[n][m] -= arr[n][m]//5
                    result -= arr[n][m]//5


R, C, T = map(int, input().split())  # R세로, C 가로, T 시간
arr = [list(map(int, input().split())) for _ in range(R)]
final_arr = [[0]*C for _ in range(R)]

coordinate = []

cleaner = []

result = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            final_arr[i][j] += arr[i][j]
            result += arr[i][j]
            coordinate.append([i, j])
        if arr[i][j] == -1:
            final_arr[i][j] += arr[i][j]
            cleaner.append([i, j])

dust(coordinate)

for z in final_arr:
    print(z)

print(R, C)

# 2번 공기청정기 작동 R = 세로, C = 가로
for check in range(1, T):
    if check <= R - 2 - cleaner[1][0]:
        cy = cleaner[1][0] + check  # 3 + 3
        cx = cleaner[1][1]
        result -= final_arr[cy][cx]
    else:
        break

if R - 1 - cleaner[1][0] < T:
    for check in range(1, T-R+cleaner[1][0]+1+1):
        if check <= C - 1:
            cy = R - 1
            cx = 0 + check
            result -= final_arr[cy][cx]

# if R - 1 - cleaner[1][0] + C - 1 <= T:
#     for check in range(1, R - 1 - cleaner[1][0]):
#         cy = R - check
#         cx = C - 1
#         result -= final_arr[cy][cx]
#
# if 2*(R - 1 - cleaner[1][0]) + C - 1 <= T:
#     for check in range(1, C-1):
#         cy = cleaner[1][0]
#         cx = C - check
#         result -= final_arr[cy][cx]

print(result)

