import sys
sys.stdin = open('1967_diameter_of_tree_input.txt')
from collections import deque


def bfs(start):
    q = deque([start])
    while q:
        cost, node = q.popleft()
        for check in edge[node]:
            nd = check[1]
            dist = check[0]
            if visited[nd] == 0:
                visited[nd] += visited[node] + dist
                q.append([dist, nd])


def bfs2(start):
    q = deque([start])
    while q:
        cost, node = q.popleft()
        for check in edge[node]:
            nd = check[1]
            dist = check[0]
            if visited_2[nd] == 0:
                visited_2[nd] += visited_2[node] + dist
                q.append([dist, nd])


N = int(input())

edge = [[] for _ in range(N+1)]
visited = [0] * (N+1)
visited[1] = 0


for i in range(N-1):
    n, m, distance = map(int, input().split())
    edge[n].append([distance, m])
    edge[m].append([distance, n])


bfs([0, 1])
idx = 0
max_distance = 0

for i in range(1, N+1):
    if max_distance <= visited[i]:
        max_distance = visited[i]
        idx = i

print(idx, max_distance)

visited_2 = [0] * (N + 1)
visited_2[idx] = 1

bfs2([0, idx])

print(edge)

print(visited)
print(visited_2)
print(max(visited_2[1:]) -1)