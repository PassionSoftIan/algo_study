import sys
sys.stdin = open('1937_greedy_panda_input.txt')


def dfs(stack):
    global count, info_count
    stack = [stack]
    n, m = stack.pop()
    check[n][m] = 1
    for k in range(4):
        ny, nx = n + dy[k], m + dx[k]
        if 0 <= ny < N and 0 <= nx < N:
            if visited[ny][nx] == 0:
                if arr[ny][nx] > arr[n][m]:
                    if info[ny][nx] > 0:
                        if info_count < info[ny][nx]:
                            info_count = info[ny][nx] + 1
                        continue
                    visited[ny][nx] = 1
                    count += 1
                    dfs([ny, nx])
                    if info_count <= count:
                        info_count = count
                    count -= 1
                    visited[ny][nx] = 0


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
info = [[0] * N for _ in range(N)]
check = [[0] * N for _ in range(N)]

max_count = 0

count = 1

for i in range(N):
    for j in range(N):
        info_count = 0
        if check[i][j] == 0:
            visited[i][j] = 1
            dfs([i, j])
            visited[i][j] = 0
            info[i][j] = info_count
            max_count = max(max_count, info_count)
for i in info:
    print(i)
print(max_count)

'''
memoization을 하기 위해서 info 값에 이전 값을 저장 후 추후 backtracking으로 탐색하는
지점은 그 이전 값을 보고 판단할 수 있는 방식을 차용 한다.

이를 위해서는 함수가 호출 됐을 때 memo의 값이 0 이상일 경우 해당 값을 더하고 바로 return을 해주는 방식을 사용
'''