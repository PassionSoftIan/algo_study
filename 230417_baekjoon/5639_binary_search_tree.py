import sys
sys.stdin = open('5639_binary_search_tree_input.txt')

tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break

print(tree)

