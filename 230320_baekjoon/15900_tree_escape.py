import sys
sys.stdin = open('15900_tree_escape_input.txt')

def dfs(stack):
    global count
    node = stack
    s = node.pop()
    visited[s] = 1
    for i in edge[s]:
        if visited[i] == 1:
            continue
        if visited[i] == 0:
            visited[i] = 1
            dfs([edge[s][i]])
            return
    if node == 1:
        count += 1
        return
    if 1 in edge[s]:
        count += 1
        return
    else:
        for u in range(len(edge[s])):
            count += 1
            dfs([edge[s][u]])
            return


N = int(input())
V = N-1
edge = [[]*N for i in range(N+1)]
visited = [0] * (N+1)
count = 0
for i in range(V):
    n, m = map(int, input().split())
    edge[n].append(m)
    edge[m].append(n)
print(edge)


stack = []
for i in range(1, N+1):
    for j in range(len(edge[i])):
        if edge[i][j] != 1 and visited[edge[i][j]] == 0:
            visited[edge[i][j]] += 1
            stack.append(edge[i][j])
            dfs(stack)

if count % 2 == 0:
    print('No')
    print(count)
else:
    print('Yes')
    print(count)