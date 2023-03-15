import sys
sys.stdin = open('2493_tower_input.txt')

N = int(input())

tower = list(map(int, input().split()))






# result = [0]
# for i in range(1, N):
#     count = 0
#     r_count = 0
#     for j in range(i-1, -1, -1):
#         if tower[i] < tower[j]:
#             count = j+1
#             r_count += 1
#             result.append(count)
#             break
#     if r_count == 0:
#         result.append(0)
#
# print(*result)