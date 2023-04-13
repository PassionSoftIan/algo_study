import sys
sys.stdin = open('14938_seokang_ground_input.txt')
from heapq import heappop, heappush


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


N, M, R = map(int, input().split())

edge = [[] for _ in range(N+1)]
visited = [int(1e9)] * (N+1)
ground = list(map(int, input().split()))

for nc in range(1, R+1):
    start, end, distance = map(int, input().split())
    edge[start].append([distance, end])
    edge[end].append([distance, start])