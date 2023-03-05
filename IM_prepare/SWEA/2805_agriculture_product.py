import sys
sys.stdin = open('2805_agriculture_product_input.txt')

dx = [1, -1]

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    S = N//2
    arr = [list(map(int, input())) for _ in range(N)]
    result = 0
    for i in range(N):
        if 0 <= i <= S:
            for k in range(2):
                for p in range(i+1):
                    nx = S + p * dx[k]
                    if 0 <= nx < N:
                        if k == 1 and p == 0:
                            continue
                        else:
                            result += arr[i][nx]
        if S < i <N:
            for k in range(2):
                for p in range(N-i):
                    nx = S + p * dx[k]
                    if 0 <= nx < N:
                        if k == 1 and p == 0:
                            continue
                        else:
                            result += arr[i][nx]
    print(f'#{tc} {result}')