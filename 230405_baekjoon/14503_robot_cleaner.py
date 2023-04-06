import sys
sys.stdin = open('14503_robot_cleaner_input.txt')


dy = [-1, 0, 1, 0] # 북 동 남 서
dx = [0, 1, 0, -1]

direction_90 = {0: 0, 1: 1, 2: 2, 3: 3, -1: 3, -2: 2, -3: 1, -4: 0}
direction_back = {0: 2, 1: 3, 2: 0, 3: 1}


def clean(info):
    global operate
    coo_info = info
    while coo_info:
        bit = 0
        n, m, d = coo_info.pop()
        if arr[n][m] == 0:
            operate += 1
            arr[n][m] = 3
        # 4방향을 보는데 90도를 회전 한 곳을 먼저 보고 차례대로 ㄱㄱ 1이면 0 3 2 1 순서로 0 이면
        for k in range(1, 5):
            ny, nx = n + dy[d-k], m + dx[d-k]
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] == 0:
                    bit = 1
                    coo_info.append([ny, nx, direction_90[d-k]])
                    break

        if bit == 0:
            by, bx = n + dy[direction_back[d]], m + dx[direction_back[d]]
            if arr[by][bx] == 1:
                return
            else:
                coo_info.append([by, bx, d])


N, M = map(int, input().split())

coordinate = [list(map(int, input().split()))]

arr = [list(map(int, input().split())) for _ in range(N)]

operate = 0

clean(coordinate)

print(operate)