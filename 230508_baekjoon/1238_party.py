import sys
sys.stdin = open('1238_party_input.txt')
from heapq import heappop, heappush


def dijkstra(first, check):
    q = []
    heappush(q, first)
    while q:
        dist, now = heappop(q)
        if visited[check][now] < dist:
            continue
        for i in edge[now]:
            total = dist + i[0]
            if total < visited[check][i[1]]:
                visited[check][i[1]] = total
                heappush(q, [total, i[1]])


N, M, X = map(int, input().split())

edge = [[] for _ in range(N+1)]

visited = [[int(1e9)]*(N+1) for _ in range(N+1)]

for mc in range(M):
    start, end, distance = map(int, input().split())
    edge[start].append([distance, end])

max_count = 0
for d in range(1, N+1):
    visited[d][d] = 0
    dijkstra([0, d], d)

for i in range(1, N+1):
    chk = visited[i][X] + visited[X][i]
    if max_count < chk:
        max_count = chk

for i in visited:
    print(i)

print(max_count)


#워셜 시간초과 남
# N, M, X = map(int, input().split())
# INF = int(1e9)
# info = [[INF] * (N+1) for _ in range(N+1)]
#
# for i in range(1, N+1):
#     info[i][i] = 0
#
# for mc in range(M):
#     start, end, distance = map(int, input().split())
#     info[start][end] = min(info[start][end], distance)
#
# for k in range(1, N+1):
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             info[i][j] = min(info[i][j], info[i][k] + info[k][j])
#
# # for i in range(1, N+1):
# #     for j in range(1, N+1):
# #         if info[i][j] == INF:
# #             info[i][j] = 0
#
# for i in info:
#     print(i)
#
# max_count = 0
#
# for i in range(1, N+1):
#     if info[i][X] + info[X][i] > max_count:
#         max_count = info[i][X] + info[X][i]
# print(max_count)