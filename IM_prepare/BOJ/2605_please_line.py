import sys
sys.stdin = open('2605_please_line_input.txt')

N = int(input())

paper = list(map(int, input().split()))
students = list(range(1, N+1))

check = list(range(1, N+1))

stack = []
stack_idx = []
for i in range(N):
    for j in range(N):
        A = students.pop()
        if A != check[i]:
            stack.append(A)
        else:
            stack_idx.append(A)
    for n in range(i-paper[i]):
        students.append(stack.pop())
    students.append(stack_idx.pop())
    while stack:
        students.append(stack.pop())
print(*students)