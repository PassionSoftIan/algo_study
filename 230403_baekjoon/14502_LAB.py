import sys
sys.stdin = open('14502_LAB_input.txt')
from collections import deque


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def wall(depth, start):
    if depth == 3:
        final_pipe.append(pipe)
        check()
        return

    for b in range(start, len(q)):
        if visited_pipe[b] == 0:
            pipe.append(q[b])
            visited_pipe[b] = 1
            wall(depth+1, b)
            pipe.pop()
            visited_pipe[b] = 0


def check():
    while final_pipe:
        one, two, three = final_pipe.popleft()
        arr[one[0]][one[1]] = 1
        arr[two[0]][two[1]] = 1
        arr[three[0]][three[1]] = 1
        for n in range(N):
            for m in range(M):
                if arr[n][m] == 2:
                    virus.append([n, m])
        infection(virus)
        arr[one[0]][one[1]] = 0
        arr[two[0]][two[1]] = 0
        arr[three[0]][three[1]] = 0


def infection(virus):
    global max_virus_count
    vrs = virus
    virus_count = 0
    visited = [[0] * M for _ in range(N)]
    while vrs:
        n, m = vrs.popleft()
        for v in range(4):
            vy, vx = n + dy[v], m + dx[v]
            if 0 <= vy < N and 0 <= vx < M:
                if arr[vy][vx] == 0 and visited[vy][vx] == 0:
                    virus_count += 1
                    visited[vy][vx] = 1
                    vrs.append([vy, vx])
    if max_virus_count < white_count - virus_count:
        max_virus_count = white_count - virus_count


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
white_count = -3
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            q.append([i, j])
        if arr[i][j] == 0:
            white_count += 1
            continue

visited_pipe = [0] * len(q)

pipe = deque()
final_pipe = deque()

virus = deque()
max_virus_count = 0

wall(0, 0)

print(max_virus_count)