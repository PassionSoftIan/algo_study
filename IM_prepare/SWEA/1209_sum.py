import sys
sys.stdin = open('1209_sum_input.txt')

for tc in range(1, 11):
    Test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = []
    count_zr = 0
    count_z = 0
    for i in range(100):
            count_x = 0
            count_y = 0
            count_z += arr[i][i]
            count_zr += arr[-i][-i] + arr[-100][-100]
            for j in range(100):
                count_x += arr[i][j]
                count_y += arr[j][i]
            result.append(count_x)
            result.append(count_y)
    print(f'#{tc} {max(result)}')



# for tc in range(1, 11):
#     Test_case = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     result = []
#     for i in range(100):
#         count_x = 0
#         count_y = 0
#         for j in range(100):
#             count_x += arr[i][j]
#             count_y += arr[j][i]
#         result.append(count_x)
#         result.append(count_y)
#
#     count_z = 0
#     for i in range(100):
#         count_z += arr[i][i]
#
#     count_zr = 0
#     for i in range(101):
#         count_zr += arr[-i][-i]
#         result.append(count_zr)
#
#
#     print(f'#{tc} {max(result)}')