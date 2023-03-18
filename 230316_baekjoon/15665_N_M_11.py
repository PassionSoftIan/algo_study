import sys
sys.stdin = open('15665_N_M_11_input.txt')

N, M = map(int, input().split())

num = sorted(list(map(int, input().split())))
result = []
def backtracking(depth):
    if depth == M:
        print(*result)
        return

    prev = 0
    for i in range(N):
        if prev != num[i]:
            result.append(num[i])
            backtracking(depth+1)
            prev = num[i]
            result.pop()


backtracking(0)