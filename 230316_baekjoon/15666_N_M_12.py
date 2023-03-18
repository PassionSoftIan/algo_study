import sys
sys.stdin = open('15666_N_M_12_input.txt')

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
result = []
visited = [0] * N
def backtracking(depth, s):
    if depth == M:
        print(*result)
        return

    prev = 0
    for i in range(s, N):
        if prev != num[i]:
            result.append(num[i])
            backtracking(depth+1, i)
            prev = num[i]
            result.pop()

backtracking(0, 0)