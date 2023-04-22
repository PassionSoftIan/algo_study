import sys
sys.stdin = open('11404_floyd_input.txt')

N = int(input())
M = int(input())

arr = [[int(1e9)]*(N+1) for _ in range(N+1)]

for mc in range(M):
    start, end, cost = map(int, input().split())
    arr[start][end] = min(arr[start][end], cost)

for i in range(N+1):
    arr[i][i] = 0

for k in range(N+1):
    for i in range(N + 1):
        for j in range(N + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(N+1):
    for j in range(N+1):
        if arr[i][j] == int(1e9):
            arr[i][j] = 0

for i in arr[1:]:
    print(*i[1:])