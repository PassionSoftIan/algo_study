import sys
sys.stdin = open('14503_robot_cleaner_input.txt')


dy = [-1, 0, 1, 0] # 북 동 남 서
dx = [0, 1, 0, -1]


def clean(c_and_i):
    global result, flag
    co_in = [c_and_i]
    while co_in:
        flag = False
        n, m, d = co_in.pop()
        if arr[n][m] == 0 and visited[n][m] == 0:
            result += 1
            visited[n][m] = 1
        for k in range(4):
            ny, nx = n + dy[k], m + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] == 0 and visited[ny][nx] == 0:
                    flag = True
                    break
        if flag == True:
            push([n, m, d])
        else:
            if N < n + dy[d-2] or n + dy[d-2] < 0 or N < m + dx[d-2] or m + dx[d-2] < 0:
                return
            if 0 <= n + dy[d-2] < N and 0 <= m + dx[d-2] < N:
                if arr[n + dy[d-2]][m + dx[d-2]] == 1:
                    return
                else:
                    co_in.append([n + dy[d-2], m + dx[d-2], d])

def push(chk):
    check = [chk]
    while check:
        n, m, d = check.pop()
        if flag == True:
            if arr[n + dy[d-1]][m + dx[d-1]] != 1 and 0 <= n + dy[d-1] < N and 0 <= m + dx[d-1] < N:
                if visited[n + dy[d-1]][m + dx[d-1]] == 0:
                    if d == 0:
                        check.append([n + dy[d-1], m + dx[d-1], 3])
                        clean(*check)
                    else:
                        check.append([n + dy[d - 1], m + dx[d - 1], d-1])
                        clean(*check)
                else:
                    if d == 0:
                        check.append([n, m, 3])
                        continue
                    else:
                        check.append([n, m, d-1])
                        continue
            else:
                if d == 0:
                    check.append([n, m, 3])
                    continue
                else:
                    check.append([n, m, d - 1])
                    continue


N, M = map(int, input().split())
coordinate_info = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
result = 0

clean(coordinate_info)

print(result)