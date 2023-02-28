import sys
sys.stdin = open('5431_minseok_assignment_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    students = list(range(1, N+1))
    result = []
    for i in students:
        if i not in arr:
            result.append(i)
    print(f'#{tc}', *result)