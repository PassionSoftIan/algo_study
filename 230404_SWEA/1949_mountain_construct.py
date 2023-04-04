import sys
sys.stdin = open('1949_mountain_construct_input.txt')
from collections import deque


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def find(q):
    global count
    queue = q
    visited = [[0]*N for _ in range(N)]
    while queue:
        n, m = queue.popleft()
        for k in range(4):
            ny, nx = n + dy[k], m + dx[k]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
                if arr[ny][nx] < arr[n][m]:
                    queue.append([ny, nx])
                    count += 1
                    visited[ny][nx] = 1

                else:
                    for work in range(1, K+1):
                        arr[ny][nx] -= work
                        if arr[ny][nx] < arr[n][m]:
                            construct([ny, nx], work, ny, nx)
                        else:
                            arr[ny][nx] += work


def construct(coordi, wrk, by, bx):
    global count
    count += 1
    operate = coordi
    while operate:
        n, m = operate.popleft()
        if arr[n][m]

    arr[by][bx] += wrk


Test_case = int(input())

for tc in range(1, Test_case+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    hight = []

    coordination = deque()
    coordination_work = deque()

    construction = deque()

    count = 0

    max_result = 0

    for rc in range(N):
        hight.extend(arr[rc])

    for hgt in range(N*N):
        if hight[hgt] == max(hight):
            coordination.append([hgt//N, hgt % N])
            # coordination_work.append([hgt//N, hgt % N])

    find(coordination)

    print(max_result)