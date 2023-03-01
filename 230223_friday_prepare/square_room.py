import sys
sys.stdin = open('square_room_input.txt')

def BFS(start):
    cnt = 0
    stack = [start]
    while stack:
        i, j = stack.pop(0)
        cnt += 1
        for k in range(4):
            nx, ny = j + dx[k], i + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[i][j] + 1 == arr[ny][nx]:
                    stack.append([ny,nx])
    return cnt

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    count = [0] * (N**2 + 1)
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            count[arr[i][j]] += BFS([i, j])

    max_result = 0
    idx = 0
    for i in range(len(count)):
        if max_result < count[i]:
            max_result = count[i]
            idx = i
    print(f'#{tc} {idx} {max_result}')