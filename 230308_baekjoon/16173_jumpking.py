import sys
sys.stdin = open('16173_jumpking_input.txt')
input = sys.stdin.readline

dx = [1, 0]
dy = [0, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def jelly():
    visited = [[0] * N for _ in range(N)]
    stack = [[0, 0]]
    while stack:
        m, n = stack.pop(0)
        value = arr[m][n]
        for k in range(2):
            tx, ty = n + value * dx[k], m + value * dy[k]
            if 0 <= tx < N and 0 <= ty < N:
                if arr[ty][tx] == -1:
                    print('HaruHaru')
                    exit()
                else:
                    if arr[ty][tx] <= 3 and visited[ty][tx] == 0:
                        visited[ty][tx] = 1
                        stack.append([ty, tx])

jelly()
print('Hing')