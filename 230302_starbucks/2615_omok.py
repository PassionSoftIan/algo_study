import sys
sys.stdin = open('2615_omok_input.txt')

def omok(start):
    stack = start
    result = []
    while stack:
        m, n = stack.pop()
        for k in range(4):
            count = 1
            for p in range(1, 5):
                ty, tx = m - dy[k], n - dx[k]
                ny, nx = m + p*dy[k], n + p*dx[k]
                if 0 <= nx < 19 and 0 <= ny < 19:
                    if 0 <= ty < 19 and 0 <= tx < 19:
                        if arr[ty][tx] == arr[m][n]:
                            continue
                    if arr[ny][nx] == arr[m][n]:
                        count += 1
                    else:
                        break
            if count == 5:
                if k == 3:
                    if k == 3:
                        if 0 <= ny + dy[k] < 19 and 0 <= nx + dx[k] < 19:
                            if arr[ny + dy[k]][nx + dx[k]] != arr[ny][nx]:
                                result.append([ny + 1, nx + 1])
                                print(arr[m][n]), print(*result[0])
                                exit()
                        else:
                            result.append([ny + 1, nx + 1])
                            print(arr[m][n]), print(*result[0])
                            exit()


                if 0 <= ny + dy[k] < 19 and 0 <= nx + dx[k] < 19:
                    if arr[ny + dy[k]][nx + dx[k]] != arr[ny][nx]:
                        result.append([m+1, n+1])
                        print(arr[m][n]), print(*result[0])
                        exit()
                else:
                    result.append([m+1, n+1])
                    print(arr[m][n]), print(*result[0])
                    exit()



dx = [1, 1, 0, -1] #오 오아 아 왼아 왼 왼위 위 오위
dy = [0, 1, 1, 1]

arr = [list(map(int, input().split())) for _ in range(19)]

start = []
for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            start.append([i,j])
            omok(start)
print('0')