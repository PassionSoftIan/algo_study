import sys
sys.stdin = open('1258_find_arr_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [[] * 100 for _ in range(100)]
    print(result)
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] != 0:
                count += 1
            if (arr[i][j] == 0 or j == N-1) and count != 0:
                result[i].append(count)
                count = 0
    # for i in range(len(result)):
    #     for j in range(len(result[i])):
    #         if result[i][j] ==

    print(result)