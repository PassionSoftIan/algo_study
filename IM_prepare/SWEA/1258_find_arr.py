import sys
sys.stdin = open('1258_find_arr_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] != 0:
                count += 1
            if (arr[i][j] == 0 or j == N-1) and count != 0:
                result.append([i,count])
                count = 0

    result.sort(key=lambda x : x[1])

    result_fin = []
    count_x = 1
    for i in range(len(result)):
        if i+1 < len(result):
            if result[i][0] + 1 == result[i+1][0] and result[i][1] == result[i+1][1]:
                count_x += 1

            if result[i][0] + 1 != result[i+1][0] or result[i][1] != result[i+1][1]:
                result_fin.append([count_x, result[i][1], result[i][1] * count_x])
                count_x = 1
        else:
            result_fin.append([count_x, result[i][1], result[i][1] * count_x])
            count_x = 1

    result_fin.sort(key=lambda x:(x[2],x[0]))

    final = []
    for i in range(len(result_fin)):
        final.append(result_fin[i][0])
        final.append(result_fin[i][1])

    print(f'#{tc}', len(result_fin), *final)