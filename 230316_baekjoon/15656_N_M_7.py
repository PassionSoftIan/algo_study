import sys
sys.stdin = open('15656_N_M_7_input.txt')

N, M = map(int, input().split())
num = sorted(list(map(int,input().split())))
result = []
def backtracking(depth):
    if depth == M:
        print(*result)
        return

    for i in range(N):
        result.append(num[i])
        backtracking(depth+1)
        result.pop()

backtracking(0)