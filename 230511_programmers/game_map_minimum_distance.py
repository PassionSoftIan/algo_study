from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(maps, q):
    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]
    q = deque([q])
    while q:
        n, m, count = q.popleft()
        for k in range(4):
            ny, nx = n + dy[k], m + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == 0:
                    if maps[ny][nx] == 1:
                        if ny == N - 1 and nx == M - 1:
                            return count + 2
                        q.append([ny, nx, count + 1])
                        visited[ny][nx] = 1
    return -1

def solution(maps):
    maps = maps
    answer = bfs(maps, [0, 0, 0])
    return answer