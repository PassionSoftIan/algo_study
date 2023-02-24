import sys
sys.stdin = open('11725_find_tree_parents_input.txt')
input = sys.stdin.readline

Test_case = int(input())
for tc in range(Test_case):
    V = int(input())
    node = [[] for _ in range(V+1)]
    sort = [0] * (V+1)

    for _ in range(V-1):
        p, c = map(int, input().split())
        node[c].append(p)
        node[p].append(c)
    print(node)
    new = []

    for i in range(V+1):
        for j in range(V+1):
            new.append(node[i][j])
    print(new)

    # for _ in range(V, 0, -1):



    # print(node)
    # # for i in range(2, V+1):
    #     # print(node[i][0])


# E = V - 1
# edge = [list(map(int, input().split())) for _ in range(E)]
# arr = [[0] * (V+1) for _ in range(V+1)]
# stack = [1]
# result = [0] * (V+1)
# for i in range(len(edge)):
#     arr[edge[i][0]][edge[i][1]] += 1
#     arr[edge[i][1]][edge[i][0]] += 1
# for i in edge:
#     print(i)
# for i in arr:
#     print(i)
#
# while stack:
#     i = stack.pop()
#     for j in range(1, V+1):
#         if arr[i][j] == 1:
#             stack.append(j)
#             result[j] = i
#             arr[j][i] = 0
#             arr[i][j] = 0
# for i in range(2, V+1):
#     print(result[i])