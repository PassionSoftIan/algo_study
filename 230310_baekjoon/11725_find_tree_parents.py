import sys
sys.stdin = open('11725_find_tree_parents_input.txt')

N = int(input())

tree = [[]] * (N+1)

print(tree)

for nc in range(N-1):
    c, p = map(int, input().split())
