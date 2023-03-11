import sys
sys.stdin = open('5639_binary_tree_input.txt')

preorder_node = []

for i in range(9):
    preorder_node.append(int(input()))

print(preorder_node)

