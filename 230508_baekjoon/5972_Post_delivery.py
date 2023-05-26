import sys
sys.stdin = open('5972_Post_delivery_input.txt')
from heapq import heappop, heappush


def dijkstra(first):
    q = []
    heappush(q, first)
    while q:
        dist, now = heappop(q)
        if visited[now] < dist:
            continue
        for i in edge[now]:
            total = dist + i[0]
            if total < visited[i[1]]:
                visited[i[1]] = total
                heappush(q, [total, i[1]])


N, M = map(int, input().split())

edge = [[] for _ in range(N+1)]

visited = [int(1e9)] * (N+1)

for mc in range(M):
    start, end, distance = map(int, input().split())
    edge[start].append([distance, end])
    edge[end].append([distance, start])

visited[1] = 0
dijkstra([0, 1])

# print(edge)
print(visited[N])