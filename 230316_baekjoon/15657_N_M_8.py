import sys
sys.stdin = open('15657_N_M_8_input.txt')

N, M = map(int, input().split())

num = sorted(list(map(int, input().split())))
result = []
def backtracking(depth, s):
    if depth == M:
        print(*result)
        return

    for i in range(s, N):
        result.append(num[i])
        backtracking(depth+1, i)
        result.pop()


backtracking(0,0)