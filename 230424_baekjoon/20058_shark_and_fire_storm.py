import sys
sys.stdin = open('20058_shark_and_fire_storm_input.txt')

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def direction(s):
    for i in range(0, 2**N, 2**s):
        for j in range(0, 2**N, 2**s):
            coordinate.append([i, j])
    spin(coordinate, 2**s)


def spin(start, counting):
    start = start
    count = 0
    while start:
        n, m = start.pop()
        info = 0
        if count != (counting**2):
            ny, nx = n + dy[info], m + dx[info]
            if 0 <= ny < n + counting and 0 <= nx < m + counting:
                arr_2[ny][nx] = arr_1[n][m]
                count += 1
            else:
                info = (info + 1) % 4


N, T = map(int, input().split())
arr_1 = [list(map(int, input().split())) for _ in range(2**N)]
S = list(map(int, input().split()))

arr_2 = [[0]*(2**N) for _ in range(2**N)]

coordinate = []

for sc in range(T):
    direction(S[sc])

print(coordinate)

for i in arr_2:
    print(i)