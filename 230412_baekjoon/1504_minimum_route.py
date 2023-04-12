import sys
sys.stdin = open('1504_minimum_route_input.txt')
from heapq import heappop, heappush


def dijkstra(go):
    global result1, result2, count_0, count_1
    visited = [int(1e9)] * (N + 1)
    visited[go[1]] = 0
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
    if go[1] == 1:
        if count_0 == 0:
            result1 += visited[exam_node1]
            result2 += visited[exam_node2]
            count_0 += 1
            return
        if count_0 == 1:
            result1 += visited[exam_node2]
            result2 += visited[N]
            count_0 += 1
            return
        if count_0 == 2:
            result1 += visited[N]
            result2 += visited[exam_node1]
            count_0 += 1
            return
    if go[1] == exam_node1:
        if count_1 == 0:
            result1 += visited[exam_node2]
            result2 += visited[N]
            count_1 += 1
            return
        if count_1 == 1:
            result1 += visited[N]
            result2 += visited[exam_node1]
            return
    if go[1] == exam_node2 and exam_node1 != exam_node2:
        result1 += visited[N]
        result2 += visited[exam_node1]


N, E = map(int, input().split())

edge = [[] for _ in range(N+1)]
for node in range(E):
    start, end, distance = map(int, input().split())
    edge[start].append([distance, end])
    edge[end].append([distance, start])

exam_node1, exam_node2 = map(int, input().split())

result1 = 0
result2 = 0

count_0 = 0
count_1 = 0

dijkstra([0, 1])
dijkstra([0, exam_node1])
dijkstra([0, exam_node2])

if result1 > int(1e9) and result2 > int(1e9):
    print(-1)
else:
    print(min(result1, result2))


# def dijkstra(go):
#     visited = [int(1e9)] * (N + 1)
#     visited[go[1]] = 0
#     heap = []
#     heappush(heap, go)
#     while heap:
#         cost, now = heappop(heap)
#         if visited[now] < cost:
#             continue
#         for check in edge[now]:
#             total = cost + check[0]
#             if total < visited[check[1]]:
#                 visited[check[1]] = total
#                 heappush(heap, [total, check[1]])
#     return visited
#
#
# N, E = map(int, input().split())
#
# edge = [[] for _ in range(N+1)]
#
# for node in range(E):
#     start, end, distance = map(int, input().split())
#     edge[start].append([distance, end])
#     edge[end].append([distance, start])
#
# exam_node1, exam_node2 = map(int, input().split())
#
# a = dijkstra([0, 1])
# b = dijkstra([0, exam_node1])
# c = dijkstra([0, exam_node2])
#
# result1 = a[exam_node1] + b[exam_node2] + c[N]
# result2 = a[exam_node2] + c[exam_node1] + b[N]
#
# if result1 >= int(1e9) and result2 >= int(1e9):
#     print(-1)
# else:
#     print(min(result1, result2))