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

bit = 0
for i in range(len(tree)-1):
    if tree[i+1] > root[0]:
        bit = 1

    if bit == 0:
        if tree[i] > tree[i+1]:
            left_left.append(tree[i+1])
        else:
            left_right.append(tree[i+1])

    else:
        if tree[i] > tree[i+1]:
            right_left.append(tree[i+1])
        else:
            right_right.append(tree[i+1])

# for i in range(len(left_left)):




print(tree)
print(left_left)
print(left_right)

print(right_left)
print(right_right)