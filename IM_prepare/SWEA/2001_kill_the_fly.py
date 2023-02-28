import sys
sys.stdin = open('2001_kill_the_fly_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    max_count = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            count = 0
            for k in range(M):
                for n in range(M):
                    count += arr[i+k][j+n]
            if count > max_count:
                max_count = count
    print(f'#{tc} {max_count}')