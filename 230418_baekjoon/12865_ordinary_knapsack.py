import sys
sys.stdin = open('12865_ordinary_knapsack_input.txt')
N, K = map(int, input().split())

DP_lst = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    weight, value = map(int, input().split())
    for j in range(1, K+1):
        if weight > j:
            DP_lst[i][j] = DP_lst[i-1][j]
        else:
            DP_lst[i][j] = max(value + DP_lst[i-1][j-weight], DP_lst[i-1][j])

print(DP_lst[N][K])

# N, K = map(int, input().split())
#
# item = [list(map(int, input().split())) for _ in range(N)]
#
# DP_lst = [[0 for _ in range(K+1)] for _ in range(N+1)]
#
# for i in range(N+1):
#     for j in range(K+1):
#         if i == 0 or j == 0:
#             DP_lst[i][j] = 0
#
#         elif item[i-1][0] <= j:
#             DP_lst[i][j] = max(item[i-1][1] + DP_lst[i-1][j-item[i-1][0]],
#                                DP_lst[i-1][j])
#         else:
#             DP_lst[i][j] = DP_lst[i-1][j]
#
# print(DP_lst[N][K])

# for i in item:
#     print(i)
#
print('---DP_lst')

for i in DP_lst:
    print(i)