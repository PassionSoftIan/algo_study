import sys
sys.stdin = open('5639_binary_search_tree_input.txt')

tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break

print(tree)

root = []
right = []
left = []

flag = True
for check in range(len(tree)-1):
    if check == 0:
        root.append(tree[check])
    if flag:
        if tree[check] > tree[check+1]:
            left.append(tree[check+1])
            continue
        else:
            flag = False