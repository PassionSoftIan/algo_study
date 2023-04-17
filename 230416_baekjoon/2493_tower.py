import sys
sys.stdin = open('2493_tower_input.txt')

N = int(input())

tower = list(map(int, input().split()))
result = []

stack = []
stack.append([0, tower[0]])
result.append(0)

for i in range(1, len(tower)):
    bit = 0
    while stack:
        n, m = stack.pop()
        if tower[i] < m:
            result.append(n+1)
            stack.append([n, m])
            bit = 1
            break
    stack.append([i, tower[i]])
    if bit == 0:
        result.append(0)

print(tower)
print(stack)
print(result)