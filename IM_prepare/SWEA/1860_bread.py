import sys
sys.stdin = open('1860_bread_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M, K = map(int, input().split())
    # N은 사람 M 붕어빵 만드는데 걸리는 시간 K는 M시간에 만드는 붕어빵 개수
    time = list(map(int, input().split()))
    time_sorted = sorted(time)
    J = K / M # 1초에 붕어빵 만드는 총 개수
    count = J * time_sorted[0] - 1
    if time_sorted[0] < M:
        print(f'#{tc} Impossible')
    else:
        for i in range(1, N):
            count += (time_sorted[i] - time_sorted[i-1]) * J
            if count >= 1:
                count -= 1
                continue
            elif count < 1:
                print(f'#{tc} Impossible')
                break
        else:
            print(f'#{tc} Possible')