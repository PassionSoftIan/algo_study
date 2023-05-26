import sys
sys.stdin = open('17298_NGE_input.txt')

N = int(input())

arr = list(map(int, input().split()))
lst = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and arr[i] > arr[stack[-1]]:
        lst[stack.pop()] = arr[i]
    stack.append(i)

print(*lst)