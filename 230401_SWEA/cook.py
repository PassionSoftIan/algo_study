import sys
sys.stdin = open('cook_input.txt')

def backtracking(depth, A, B):
    global min_result, count
    if count >= 2:
        return
    if not A:
        count += 1
    if len(A) > M or len(B) > M:
        return
    if depth == N:
        if len(A) == M:
            a = 0
            b = 0
            for i in range(M):
                for j in range(M):
                    a += ingredient[A[i]][A[j]]
                    b += ingredient[B[i]][B[j]]
            if min_result > abs(a-b):
                min_result = abs(a-b)
        return

    backtracking(depth+1, A+[depth], B)
    backtracking(depth+1, A, B+[depth])


Test_case = int(input())
for tc in range(1, Test_case+1):
    N = int(input())
    M = N//2
    ingredient = [list(map(int, input().split())) for _ in range(N)]
    min_result = 1e9

    memo = []
    count = 0

    backtracking(0, [], [],)

    print(f'#{tc} {min_result}')