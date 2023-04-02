import sys
sys.stdin = open('2806_N_Queen_input.txt')

def check(depth):
    return


Test_case = int(input())

for tc in range(1, Test_case+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    print(arr)