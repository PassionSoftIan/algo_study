import sys
sys.stdin = open('2805_tree_cutting_input.txt')

N, M = map(int, input().split())

arr = list(map(int, input().split()))

top = 1
low = sum(arr)

while top <= low:
    mid = (top + low) // 2
    count = 0
    for i in arr:
        if i > mid:
            count += i - mid

    if count >= M:
        top = mid + 1

    else:
        low = mid - 1

print(low)








# def cutting():
#     if M >= sum(arr) - arr[-1]:
#         print(0)
#         return
#
#     check = len(arr)//2
#     check_count_plus = 0
#     while True:
#         count = 0
#         for i in range(check):
#             count += arr[i] - arr[check]
#
#         if count == M:
#             print(arr[check])
#             return
#
#         if count > M:
#             if check_count_plus == 0:
#                 check -= 1
#                 continue
#
#             else:
#                 print(((count - M) // check) + arr[check])
#                 return
#
#         if count < M:
#             check += 1
#             check_count_plus = 1
#             continue
#
# def quick_sort(arr, left, right):
#     if left < right:
#         mid = cal(arr, left, right)
#         quick_sort(arr, left, mid - 1)
#         quick_sort(arr, mid + 1, right)
#
# def cal(arr, left, right):
#     i = left - 1
#     j = left
#     pivot = arr[right]
#     while j < right:
#         if pivot > arr[j]:
#             i += 1
#             if i < j:
#                 arr[i], arr[j] = arr[j], arr[i]
#
#         j += 1
#     arr[i + 1], arr[right] = arr[right], arr[i+1]
#     return i + 1
#
# N, M = map(int, input().split())
#
# arr = list(map(int, input().split()))
# quick_sort(arr, 0, len(arr)-1)
#
# arr = sorted(arr, reverse=True)
# print(arr)
#
# counting = 1
# for i in range(len(arr)-1):
#     if arr[i] == arr[i+1]:
#         counting += 1
# if counting == N:
#     print(arr[0] - M)
#     exit()
#
# cutting()