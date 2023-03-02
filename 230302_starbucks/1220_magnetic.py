import sys
sys.stdin = open('1220_magnetic_input.txt')

# 1은 S극 2는 N극

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    q_i= [[] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[j][i] != 0:
                q_i[i].append(arr[j][i])
    count = 0
    for i in range(len(q_i)):
        A = q_i.pop(0)
        if len(A) == 1:
            continue
        while A[0] == 2:
            A.pop(0)
        while A[-1] == 1:
            A.pop()
        while A:
            B = A.pop(0)
            if A:
                C = A[0]
            if B == 1 and C == 2:
                count += 1
                if A:
                    A.pop(0)
            else:
                continue

    print(f'#{tc} {count}')