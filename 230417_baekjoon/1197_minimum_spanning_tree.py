import sys
sys.stdin = open('1197_minimum_spanning_tree_input.txt')

from collections import deque


def union(number):
    if number != node[number]:
        node[number] = union(node[number])
    return node[number]


V, E = map(int, input().split())  # V = 정점 개수, E = 간선 개수

edge = deque([list(map(int, input().split())) for _ in range(E)])

print(edge)
node = [_ for _ in range(V+1)]

deque(sorted(edge, key=lambda x: x[2]))
print(edge)
result = 0

# Union 과정
while edge:
    n, m, cost = edge.popleft()
    start = union(n)
    end = union(m)
    if start != end:
        if start > end:
            node[start] = end
        else:
            node[end] = start
        result += cost

print(result)
# def union(number):
#     if number != node[number]:
#         node[number] = union(node[number])
#     return node[number]
#
#
# V, E = map(int, input().split()) # V = 정점 개수, E = 간선 개수
#
# edge = [list(map(int, input().split())) for _ in range(E)]
#
# node = [_ for _ in range(V+1)]
#
# edge.sort(key=lambda x : x[2], reverse=True)
#
# result = 0
# # Union 과정
#
# while edge:
#     n, m, cost = edge.pop()
#     start = union(n)
#     end = union(m)
#     if start != end:
#         if start > end:
#             node[start] = end
#         else:
#             node[end] = start
#         result += cost
#
# print(result)