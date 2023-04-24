import sys
sys.stdin = open('5639_binary_search_tree_input.txt')

tree = []

while True:
    try:
        tree.append(int(input()))

    except:
        break

root = [tree[0]]

left_left = []
left_right = []

right_left = []
right_right = []

left = []
right = []

bit = 0
for i in range(len(tree)-1):
    if tree[i+1] > root[0]:
        bit = 1

    if bit == 0:
        if tree[i] > tree[i+1]:
            left_left.append(tree[i+1])
            left.append(tree[i+1])
        else:
            left_right.append(tree[i+1])
            left.append(tree[i+1])

    else:
        if tree[i] > tree[i+1]:
            right_left.append(tree[i+1])
            right.append(tree[i+1])
        else:
            right_right.append(tree[i+1])
            right.append(tree[i+1])

while left_left or left_right:
    if left_left:
        n = left_left.pop()
        print(n)
    if left_right:
        m = left_right.pop(0)
        print(m)

while right_left or right_right:
    if len(right_left) < len(right_right):
        if right_right:
            m = right_right.pop()
            print(m)

        if right_left:
            n = right_left.pop(0)
            print(n)
    else:
        if right_right:
            m = right_right.pop()
            print(m)

        if right_left:
            n = right_left.pop(0)
            print(n)



print(*root)


# print(tree)
# print(left_left)
# print(left_right)
#
print(right_left)
print(right_right)
#
# print(left)