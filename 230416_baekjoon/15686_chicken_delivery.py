import sys
sys.stdin = open('15686_chicken_delivery_input.txt')


def backtracking(depth, s):
    if depth == M:
        check(result)
        return

    for c in range(s, len(chicken)):
        if visited[c] == 0:
            result.append(chicken[c])
            visited[c] = 1
            backtracking(depth+1, c)
            visited[c] = 0
            result.pop()


def check(rlt):
    global min_result
    chk = rlt
    temp = 0
    for dis in home:
        count = int(1e9)
        for cc in chk:
            y, x = dis[0], dis[1]
            ny, nx = cc[0], cc[1]
            distance = abs(y-ny) + abs(x-nx)
            if count > distance:
                count = distance
        temp += count
    if min_result > temp:
        min_result = temp


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

chicken = []
home = []

result = []

min_result = int(1e9)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i, j])
        if arr[i][j] == 1:
            home.append([i, j])

visited = [0]*len(chicken)
backtracking(0, 0)

print(min_result)