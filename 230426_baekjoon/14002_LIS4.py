import sys
sys.stdin = open('14002_LIS4_input.txt')

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
lst = []
result = 0
for i in range(1, N):
    temp = []
    rlt = 0
    for j in range(i):
        if arr[j] < arr[i]:
            if dp[i] <= dp[j]+1:
                if dp[i] == dp[j]+1 and temp[-1] > arr[j]:
                    temp.pop()
                    temp.append(arr[j])
                    rlt = max(dp[i], rlt)
                    print(f'{i} {j}', dp, dp[i], arr[i], arr[j])
                else:
                    dp[i] = dp[j]+1
                    rlt = max(dp[i], rlt)
                    temp.append(arr[j])
                    print(f'{i} {j}', dp, dp[i], arr[i], arr[j])

    temp.append(arr[i])
    if rlt > result:
        result = rlt
        lst = temp

print(max(dp))

if not lst:
    print(arr[0])
else:
    print(*lst)