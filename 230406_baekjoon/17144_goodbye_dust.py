import sys
sys.stdin = open('17144_goodbye_dust_input.txt')


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





print(result)

