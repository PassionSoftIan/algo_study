import sys
sys.stdin = open('1260_DFS_BFS_input.txt')

def DFS(node_lst):
    result = []
    stack = node_lst
    while stack:
        m = stack.pop()
        result.append(m)
        visited[m] = 1
        if visited[m] != 1:



N, M, V = map(int, input().split())

node = [[] * (N+1) for _ in range(N+1)]
node_lst = list(range(1, N+1))
visited = [[0] * (N+1) for _ in range(N+1)]

print(node)

for i in range(M):
    p, c = map(int, input().split())
    node[p].append(c)
    node[c].append(p)

DFS(node_lst)
BFS(node_lst)


print(node)