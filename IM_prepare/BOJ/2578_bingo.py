import sys
sys.stdin = open('2578_bingo_input.txt')

def bingo(start):
    global result_fin
    global count
    fin_count = 0
    stack = [start]
    result = []
    while stack:
        m, n = stack.pop()
        for k in range(4):
            count_l = 0
            for p in range(5):
                ny, nx = m + p * dy[k], n + p * dx[k]
                if 0 <= ny < 5 and 0 <= nx < 5:
                    if arr[ny][nx] == 0:
                        count_l += 1
                        result.append([ny,nx])
            if count_l == 5:
                fin_count += 1
                if fin_count == 3:
                    print(count)
                    exit()

        if n != 4 and m == 0:
            stack.append([m, n + 1])

        elif n == 4 and m == 0:
            stack.append([m + 1, 0])

        elif 3 >= m >= 1:
            stack.append([m + 1, 0])



dx = [1, 1, 0, -1] #오 오아 아 왼아
dy = [0, 1, 1, 1]

arr = [list(map(int, input().split())) for _ in range(5)]

start = [0,0]

result_fin = 0
count = 0

announcement = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        for n in range(5):
            for m in range(5):
                if announcement[i][j] == arr[n][m]:
                    arr[n][m] = 0
                    count += 1
                    bingo(start)