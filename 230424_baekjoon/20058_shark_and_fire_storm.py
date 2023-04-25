import sys
sys.stdin = open('20058_shark_and_fire_storm_input.txt')


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def spin(s, time):
    visited = [[0]*(2**N) for _ in range(2**N)]
    if s == 0:
        for i in range(0, 2 ** N):
            for j in range(0, 2 ** N):
                visited[i][j] = arr_1[i][j]
                arr_1[i][j] = 0
        storm(visited)
        return

    for i in range(0, 2**N, 2**s):
        for j in range(0, 2**N, 2**s):
            for n in range(2**s):
                for m in range(2**s):
                    visited[i+n][j+m] = arr_1[i+2**s-m-1][j+n]
                    arr_1[i+2**s-m-1][j+n] = 0
    storm(visited)


def storm(arr):
    global final_result
    arr = arr
    for i in range(2**N):
        for j in range(2**N):
            if arr[i][j] == 0:
                continue
            count = 0
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                if 0 <= ny < 2**N and 0 <= nx < 2**N and arr[ny][nx] > 0:
                    count += 1
            if count < 3:
                arr_1[i][j] = arr[i][j] - 1
            else:
                arr_1[i][j] = arr[i][j]


def find_ice(arr):
    global final_result, max_result
    arr = arr
    coordinate = []
    for i in range(2**N):
        for j in range(2**N):
            if arr[i][j] == 0:
                continue
            else:
                final_result += arr[i][j]
                coordinate.append([i, j])
    if not coordinate:
        return

    while coordinate:
        n, m = coordinate.pop()
        stack = [[n, m]]
        count = 0
        info = [[0] * (2 ** N) for _ in range(2 ** N)]
        while stack:
            n, m = stack.pop()
            for k in range(4):
                ny, nx = n + dy[k], m + dx[k]
                if 0 <= ny < 2 ** N and 0 <= nx < 2 ** N and arr_1[ny][nx] > 0:
                    if info[ny][nx] == 0:
                        stack.append([ny, nx])
                        info[ny][nx] = 1
                        count += 1
        if max_result < count:
            max_result = count
        if max_result == (2 ** N)*(2 ** N):
            return


N, T = map(int, input().split())
arr_1 = [list(map(int, input().split())) for _ in range(2**N)]
S = list(map(int, input().split()))


final_result = 0

max_result = 0

for sc in range(T):
    spin(S[sc], sc)
find_ice(arr_1)


# print('----arr_1')
# for z in arr_1:
#     print(z)

print(final_result)
print(max_result)