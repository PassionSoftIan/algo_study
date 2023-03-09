import sys
sys.stdin = open('13913_hide_seek4_input.txt')
from collections import deque

def cal(N, M, c):
    que = deque([[N, c]])
    target = M
    t = 0
    while que:
        i, c = que.popleft()
        if i == target:
            t = i
            print(c)
            break
        else:
            if 0 <= i * 2 <= 100000:
                if arr[i*2] == 0:
                    que.append([i * 2, c + 1])
                    arr[i*2] = 1
                    trace[i*2] = i

            if 0 <= i + 1 <= 100000:
                if arr[i+1] == 0:
                    que.append([i + 1, c + 1])
                    arr[i+1] = 1
                    trace[i+1] = i

            if 0 <= i - 1 <= 100000:
                if arr[i-1] == 0:
                    que.append([i - 1, c + 1])
                    arr[i-1] = 1
                    trace[i-1] = i

    fin = []
    for v in range(c+1):
        fin.append(t)
        t = trace[t]
    print(*fin[::-1])
    exit()


N, M = map(int, input().split())

arr = [0] * 100001
trace = [0] * 100001
c = 0
cal(N, M, c)