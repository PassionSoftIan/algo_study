import sys
sys.stdin = open('5639_binary_tree_input.txt')

preorder_node = [0]

while True:
    try:
        preorder_node.append(int(input()))
    except:
        break

print(preorder_node)

left = []
right = []

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






# for i in range(9):
#     preorder_node.append(int(input()))

# tree = [[0, 0, 0] for _ in range(len(preorder_node))]
# left = []
# right = []
#
# print(preorder_node)
#
# for i in range(1, len(preorder_node)-1):
#     tree[i][0] = preorder_node[i]
#     if preorder_node[i] > preorder_node[i+1]:
#         tree[i][1] = i+1
#     elif preorder_node[i-1] < preorder_node[i+1]:
#         tree[i-1][2] = i+1
#
# print(tree)





# fin_l = sorted(left)
# fin_r = sorted(right)
# print(fin_l)
# print(fin_r)
#
# while fin_r and fin_l:
#     print(fin_l.pop(0))
#     print(fin_r.pop(0))
#
# print(preorder_node[1])
#
# print(preorder_node[1])
# print(left, right)