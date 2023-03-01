import sys
sys.stdin = open('2477_yellow_mellon_input.txt')
N = int(input())
arr= [list(map(int,input().split())) for _ in range(6)]

count_west_lst = []
count_east_lst = []
count_north_lst = []
count_south_lst = []

for i in range(6):
    if arr[i][0] == 1:
        count_east_lst.append(arr[i][1])
    if arr[i][0] == 2:
        count_west_lst.append(arr[i][1])
    if arr[i][0] == 3:
        count_south_lst.append(arr[i][1])
    if arr[i][0] == 4:
        count_north_lst.append(arr[i][1])

if max(count_north_lst) > max(count_south_lst):
    A = max(count_north_lst)
    C = max(count_south_lst)
if max(count_north_lst) < max(count_south_lst):
    A = max(count_south_lst)
    C = max(count_north_lst)
if max(count_east_lst) > max(count_west_lst):
    B = max(count_east_lst)
    D = max(count_west_lst)
if max(count_east_lst) < max(count_west_lst):
    B = max(count_west_lst)
    D = max(count_east_lst)

C = (A*B) - ((A-C) * (B-D))

print(N*C)
