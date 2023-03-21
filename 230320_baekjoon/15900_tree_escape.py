import sys
sys.stdin = open('15900_tree_escape_input.txt')

N = int(input())
V = N-1
edge = [[]*N for i in range(N+1)]
visited = [-1] * (N+1)
visited[1] = 0

count = 0
for i in range(V):
    n, m = map(int, input().split())
    edge[n].append(m)
    edge[m].append(n)



stack = [1]
while stack:
    r = stack.pop()
    check = True
    for next_node in edge[r]:
        if visited[next_node] == -1:
            visited[next_node] = visited[r] + 1
            stack.append(next_node)
            check = False

    if check is True:
        count += visited[r]

if count % 2 == 0:
    print('No')
else:
    print('yes')
