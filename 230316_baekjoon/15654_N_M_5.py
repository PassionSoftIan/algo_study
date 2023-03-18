import sys
sys.stdin = open('15654_N_M_5_input.txt')

N, M = map(int, input().split())

num = sorted(list(map(int, input().split())))

num_lst = []

def backtracking(depth):
    if len(num_lst) == M:
        print(*num_lst)
        return
    for i in range(N):
        if num[i] not in num_lst:
            num_lst.append(num[i])
            backtracking(depth+1)
            num_lst.pop()

backtracking(0)