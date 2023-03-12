import sys
sys.stdin = open('5639_binary_tree_input.txt')

preorder_node = [0]

for i in range(9):
    preorder_node.append(int(input()))

left = []
right = []

print(preorder_node)

for i in range(1, len(preorder_node)-1):
    if preorder_node[i] > preorder_node[i+1]:
        left.append(preorder_node[i+1])
    else:
        right.append(preorder_node[i+1])

fin_l = sorted(left)
fin_r = sorted(right)

while fin_r and fin_l:
    print(fin_l.pop(0))
    print(fin_r.pop(0))

print(preorder_node[1])
print(left, right)