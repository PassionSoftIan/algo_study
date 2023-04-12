import sys
sys.stdin = open('4485_zelda_input.txt')
from heapq import heappop, heappush


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dijkstra(go):
    heap = []
    heappush(heap, go)
    while heap:
        cost, now = heappop(heap)
        if visited[now] < cost:
            continue
        for check in edge[now]:
            total = cost + check[0]
            if total < visited[check[1]]:
                visited[check[1]] = total
                heappush(heap, [total, check[1]])


count = 0
while True:
    N = int(input())
    if N == 0:
        break

    if N != 0:
        count += 1

    arr = [list(map(int, input().split())) for _ in range(N)]
    edge = [[] for _ in range((N*N)+1)]
    visited = [int(1e9)] * ((N*N)+1)

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                if 0 <= ny < N and 0 <= nx < N:
                    edge[(i*N)+j+1].append([arr[ny][nx], (ny*N+nx+1)])

    dijkstra([arr[0][0], 1])

    print(f'Problem {count}: {visited[N*N]}')