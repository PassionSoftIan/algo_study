import sys
sys.stdin = open('17245_server_room_input.txt')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

arr_lst = []

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            arr_lst.append(arr[i][j])

if len(arr_lst) == 0:
    print(0)
    exit()

start = 1
end = max(arr_lst)
total_half = sum(arr_lst)/2
check = False

if type(total_half) == float:
    total_half = int(total_half) + 1

while start <= end:
    count = 0
    mid = (start + end) // 2
    for com in arr_lst:
        if com >= mid:
            count += mid
        else:
            count += com

    if count <= total_half:
        check = True
        start = mid + 1

    else:
        check = False
        end = mid - 1


if check:
    print(start)
else:
    print(end)