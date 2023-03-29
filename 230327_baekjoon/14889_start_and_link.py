import sys
sys.stdin = open('14889_start_and_link_input.txt')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

num = list(range(N-1))

result = []
def status(depth):
    if depth == N-1:
