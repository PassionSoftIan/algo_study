import sys
sys.stdin = open('1949_mountain_construct_input.txt')


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def check(stk):
    global max_result, result

    stack = [stk]

    n, m = stack.pop()
    for k in range(4):
        ny, nx = n + dy[k], m + dx[k]
        if 0 <= ny < N and 0 <= nx < N:
            if arr[n][m] > arr[ny][nx]:
                check([ny, nx])
            if arr[n][m] < arr[ny][nx]:
                if arr[ny][nx] - K < arr[n][m]:
                    continue
                else:
                    arr[ny][nx] -= arr[ny][nx] - arr[n][m] - 1
                    result += construct([ny, nx])
                    arr[ny][nx] += arr[ny][nx] - arr[n][m] - 1
    if max_result < result:
        max_result = result


def construct(stk_c):
    result_c = 1
    stack_c = [stk_c]
    while stack_c:
        nc, mc = stack_c.pop()
        for c in range(4):
            cy, cx = nc + dy[c], mc + dx[c]
            if 0 <= cy < N and 0 <= cx < N:
                if arr[nc][mc] > arr[cy][cx] and visited[cy][cx] == 0:
                    visited[cy][cx] = 1
                    result_c += 1
    return result_c


Test_case = int(input())

for tc in range(1, Test_case+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    hight = []

    coordination = []
    coordination_work = []

    construction = []

    result = 0

    max_result = 0

    for rc in range(N):
        hight.extend(arr[rc])

    for hgt in range(N*N):
        if hight[hgt] == max(hight):
            coordination.append([hgt//N, hgt % N, 0])

    for cd in coordination:
        visited = [[0] * N for _ in range(N)]
        visited[cd[0]][cd[1]] = 1
        check(cd)

    print(max_result)