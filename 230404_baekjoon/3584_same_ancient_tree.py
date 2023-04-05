import sys
sys.stdin = open('3584_same_ancient_tree_input.txt')

Test_case = int(input())
for tc in range(Test_case):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    result = 0

    for nc in range(N-1):
        n, m = map(int, input().split())
        tree[n].append(m)
        tree[m].append(n)

    q_1, q_2 = map(int, input().split())

    for i in tree[1]:
        check = [[0] for _ in range(N+1)]
        count = N
        stack = [i]
        flag = True
        while stack:
            node = stack.pop()
            if tree[node]
            if visited[node] == 0:
                visited[node] = 1
                stack.append(tree[node])
                check[count] = tree[node]
                count -= 1


    print(tree)
    print(q_1, q_2)
    print(result)