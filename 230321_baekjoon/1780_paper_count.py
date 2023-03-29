import sys
sys.stdin = open('1780_paper_count_input.txt')

def cut(start, end):
    for i in range(start, end):
        for j in range(start, end - 1):
            if arr[i][j] != arr[i][j + 1]:
                cut(start, end//3)
                return
            else:
                continue
        cut(start + 3, end)
    return end

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)

print(cut(0, N))