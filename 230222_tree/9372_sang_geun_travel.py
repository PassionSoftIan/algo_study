import sys
sys.stdin = open('9372_sang_geun_travel_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(M)]
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    stack = [1]
    visited = [0] * (N + 1)
    for i in range(len(edge)):
        arr[edge[i][0]][edge[i][1]] = 1
        arr[edge[i][1]][edge[i][0]] = 1
    count = 0
    while stack:
        j = stack.pop()
        for i in range(1, N+1):
            if arr[j][i] == 1 and not visited[i]:
                stack.append(i)
                count += 1
                visited[i] = 1
                arr[j][i] = 0
                arr[i][j] = 0

    print(count)
    # E = N-1
    # edge = [list(map(int, input().split())) for _ in range(M)]
    # tree = [[0] * 3 for _ in range(N+1)] # 왼, 오, 부모
    # count = 0
    #
    # for i in range(E):
    #     p, c = edge[i][0], edge[i][1]
    #     if tree[p][0] == 0:
    #         tree[p][0] = c
    #     else:
    #         tree[p][1] = c
    #     tree[c][2] = p
    #     # print(p, c)
    #     print(tree)
    # root = 0
    # for i in range(1, N+1):
    #     if tree[i][2] == 0:
    #         root = i
    #         break
    # preorder(1)
    # print(count)