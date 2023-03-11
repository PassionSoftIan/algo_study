import sys
sys.stdin = open('11725_find_tree_parents_input.txt')

from collections import deque

N = int(input())

tree = [[] * N for _ in range(N+1)]
parent = [0] * (N+1)

def bfs():
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for i in tree[node]:
            if parent[i] == 0:
                parent[i] = node
                q.append(i)
    return parent


for nc in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

bfs()

for i in range(2, len(parent)):
    print(parent[i])