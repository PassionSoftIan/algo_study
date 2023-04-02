import sys
sys.stdin = open('1654_LAN_line_cutting_input.txt')

K, N = map(int, input().split())

lines = [int(input()) for _ in range(K)]

start = 1
end = max(lines)


while start <= end:
    count = 0
    mid = (start + end) // 2
    for line in lines:
        if line >= mid:
            count += line // mid

    if count >= N:
        start = mid + 1

    else:
        end = mid - 1



print(end)