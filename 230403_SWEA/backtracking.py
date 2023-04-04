import sys
sys.stdin = open('backtracking_input.txt')


def backtracking(depth):
    global min_result
    if depth == N:
        if result[0] != 0:
            return

        count = 0
        for i in result:
            if i == a:
                count += 1
            if i == b and count == 0:
                return

        rlt = arr[b][0]
        for i in range(len(result)-1):
            rlt += arr[result[i]][result[i+1]]
        if min_result > rlt:
            min_result = rlt
            return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            result.append(i)
            backtracking(depth+1)
            result.pop()
            visited[i] = 0


Test_case = int(input())

for tc in range(1, Test_case+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    a, b = map(int, input().split())

    visited = [0] * N

    result = []

    min_result = 1e9

    backtracking(0)

    print(f'#{tc} {min_result}')