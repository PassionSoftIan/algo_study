import sys
sys.stdin = open('2559_numerical_progression_input.txt')
input = sys.stdin.readline
N, K = map(int, input().split())
temp = list(map(int, input().split()))
arr = [0]*(N+1)
result = []
for i in range(N):
    arr[i+1] = arr[i] + temp[i]

for j in range(N-K+1):
    result.append(arr[j+K] - arr[j])

print(max(result))