import sys
sys.stdin = open('10159_scale_input.txt')

N = int(input())
M = int(input())

edge = [[] for _ in range(N+1)]

for mc in range(M):
    start, end = map(int, input().split())
    edge[start].append(end)

visited = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    stack = [i]
    count = 0
    while stack:
        n = stack.pop()
        if visited[i][n] == 0:
            if edge[n]:
                for j in range(len(edge[n])):
                    stack.append(edge[n][j])
            visited[i][n] = 1
            visited[n][i] = 1

for i in visited:
    print(i)

for i in range(1, N+1):
    count = 0
    for j in range(1, N+1):
        if visited[i][j] == 0:
            count += 1
    print(count)
print(edge)








# def warshall():
#     for y in range(1, N+1):
#         for x in range(1, N+1):
#             for k in range(1, N+1):
#                 info[x][k] = min(info[x][k], info[x][y] + info[y][k])
#     # for o in range(1, N+1):
#     #     for p in range(1, N+1):
#     #         if info[o][p] == INF:
#     #             info[o][p] = 0
#
#
# N = int(input())
# M = int(input())
#
# edge = [[] for _ in range(N+1)]
#
# INF = int(1e9)
#
# info = [[INF] * (N+1) for _ in range(N+1)]
#
# for i in range(1, N+1):
#     info[i][i] = 0
#
# for mc in range(M):
#     start, end = map(int, input().split())
#     info[start][end] = min(info[start][end], 1)
#
# warshall()
#
# for i in info:
#     print(i)