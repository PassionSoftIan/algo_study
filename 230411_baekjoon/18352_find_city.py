import sys
sys.stdin = open('18352_find_city_input.txt')
from heapq import heappop, heappush

N, M, K, X = map(int, input().split())

arr = [[] for _ in range(N+1)]
visited = [int(1e9)]*(N+1)

for push in range(M):
    start, end = map(int, input().split())
    arr[start].append([1, end])

visited[X] = 0


def dijkstra(s):
    q = []
    heappush(q, s)
    while q:
        cst, now = heappop(q)
        if visited[now] < cst:
            continue
        for check in arr[now]:
            compare = cst + check[0]
            if compare < visited[check[1]]:
                visited[check[1]] = compare
                heappush(q, (compare, check[1]))


dijkstra((0, X))
bit = 0
for i in range(1, len(visited)):
    if visited[i] == K:
        print(i)
        bit = 1

if bit == 0:
    print(-1)