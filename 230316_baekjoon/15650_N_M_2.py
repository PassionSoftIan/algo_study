import sys
sys.stdin = open('15650_N_M_2_input.txt')

N, M = map(int, input().split())

num = sorted(list(range(1, N+1)))

result = []
temp = []
def backtracking(depth):
    if depth == M:
        if sorted(result) not in temp:
            print(*result)
            temp.append(sorted(result))
            return
    for i in range(N):
        if num[i] not in result:
            result.append(num[i])
            backtracking(depth+1)
            result.pop()
backtracking(0)