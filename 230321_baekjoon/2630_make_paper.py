import sys
sys.stdin = open('2630_make_paper_input.txt')

def cut(x, y, end):
    global count_0, count_1

    count = 0
    color = 2
    for i in range(y, end):
        for j in range(x, end):
            if arr[i][j] == arr[y][x]:
                count += 1
                color = arr[y][x]

    if count*count == end*end and color == 0:
        count_0 += 1

    elif count*count == end*end and color == 1:
        count_1 += 1

    else:
        cut(x, y, N//2)


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
count_0 = 0
count_1 = 0


cut(0, 0, N)