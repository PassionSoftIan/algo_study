import sys
sys.stdin = open('4613_russian_flag_input.txt')


# T = int(input())
#
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     mat = [list(map(str, input())) for _ in range(N)]
#
#
#     result = []
#
#     for WB in range(1, N-2):                        #1
#         for BR in range(WB + 1, N-2):            #2
#             count = 0
#             for i in range(N):
#                 for j in range(M):
#                     if i <= WB and mat[i][j] == 'R' or i <= WB and mat[i][j] == 'B':                  #3
#                         count += 1
#                         continue
#                     if  WB < i <= BR and mat[i][j] == 'W' or  WB < i <= BR and mat[i][j] == 'R':      #4
#                         count += 1
#                         continue
#                     if  BR < i and mat[i][j] == 'W' or  BR < i and mat[i][j] == 'B':                  #5
#                         count += 1
#                         continue
#             result.append(count)                                                                      #6
#
#     print(f'#{tc} {min(result)}')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    # result = 0
    #
    # for i in range(len(arr[0])):
    #     if arr[0][i] != 'W':
    #         result += 1
    #
    # for i in range(len(arr[N-1])):
    #     if arr[N-1][i] != 'R':
    #         result += 1

    fin = []
    for w in range(0, N-2):
        for b in range(w, N-1):
            count = 0
            for i in range(N):
                for j in range(M):
                    if i <= w and arr[i][j] != 'W':
                        count += 1
                        continue
                    if w < i <= b and arr[i][j] != 'B':
                        count += 1
                    if b < i and arr[i][j] != 'R':
                        count += 1
                        continue
            fin.append(count)

    print(f'#{tc} {min(fin)}')