import sys
sys.stdin = open('2026_virus_input.txt')
def BFS(start):
    count = 0
    q = [start]
    visited[start] = 1
    while q:
        start = q.pop(0)
        for next in range(V+1):
            if mat[start][next] == 1 and not visited[next]:
                q.append(next)
                visited[next] = 1
                count += 1
    return count

V = int(input())
E = int(input())

mat = [[0] * (V+1) for _ in range(V+1)]
visited = [0] * (V+1)
for _ in range(E):
    n1, n2 = map(int, input().split())
    mat[n1][n2] = 1
    mat[n2][n1] = 1

print(BFS(1))
