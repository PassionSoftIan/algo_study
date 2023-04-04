import sys
sys.stdin = open('2819_a_grid_plate_number_series_input.txt')


def backtracking(depth, coordinate):
    stack = [coordinate]
    if depth == 6:
        char_list.add(''.join(char))
        return

    n, m = stack.pop()
    for k in range(4):
        ny, nx = n + dy[k], m + dx[k]
        if 0 <= ny < 4 and 0 <= nx < 4:
            char.append(str(arr[ny][nx]))
            backtracking(depth + 1, [ny, nx])
            char.pop()


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

Test_case = int(input())

for tc in range(1, Test_case + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    char_list = set()

    for i in range(4):
        for j in range(4):
            char = [str(arr[i][j])]
            backtracking(0, [i, j])

    print(f'#{tc} {len(char_list)}')