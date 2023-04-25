import sys
sys.stdin = open('16938_camp_prepare_input.txt')

N, L, R, X = map(int, input().split())
level = list(map(int, input().split()))

count = 0
for i in range(1, 1 << N):
    arr = []
    for j in range(N):
        if i & (1 << j):
            arr.append(level[j])
    if L <= sum(arr) <= R and max(arr) - min(arr) >= X:
        count += 1

print(count)