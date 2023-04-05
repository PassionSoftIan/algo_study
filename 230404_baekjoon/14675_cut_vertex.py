import sys
sys.stdin = open('14675_cut_vertex_input.txt')

N = int(input())
V = N-1
tree = [[] for _ in range(N+1)]
for i in range(V):
    n, m = map(int, input().split())
    tree[m].append(m)
    tree[n].append(n)

Q = int(input())
for i in range(Q):
    t, k = map(int, input().split())
    if t == 1:
        if len(tree[k]) == 1:
            print('no')
        else:
            print('yes')
    else:
        print('yes')