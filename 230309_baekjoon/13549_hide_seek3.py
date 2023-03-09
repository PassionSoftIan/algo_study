import sys
sys.stdin = open('13549_hide_seek3_input.txt')
from collections import deque

def cal(N, M, c):
    que = deque([[N, c]])
    target = M
    while que:
        i, c = que.popleft()
        if i == target:
            print(c)
            exit()
        else:
            arr[i] = 1
            if 0 <= i * 2 <= 100000:
                if arr[i*2] == 0:
                    que.appendleft([i * 2, c])
            if 0 <= i + 1 <= 100000:
                if arr[i+1] == 0:
                    que.append([i + 1, c + 1])
            if 0 <= i - 1 <= 100000:
                if arr[i-1] == 0:
                    que.append([i - 1, c + 1])



N, M = map(int, input().split())

arr = [0] * 100001
c = 0
cal(N, M, c)