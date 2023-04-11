import sys
sys.stdin = open('1916_minimum_cost_input.txt')
from heapq import heappop, heappush

N = int(input())
M = int(input())

arr = [[] for _ in range(N+1)]
visited = [int(1e9)]*(N+1)

for push in range(M):
    start, end, cost = map(int, input().split())
    arr[start].append((cost, end))

exam_start, exam_end = map(int, input().split())

visited[exam_start] = 0


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


dijkstra((0, exam_start))
print(visited[exam_end])