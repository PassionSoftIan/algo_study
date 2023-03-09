import sys
sys.stdin = open('12851_hide_seek2_input.txt')
import sys
from collections import deque

def cal(N, M, c):
    que = deque([[N, c]])
    target = M
    result = []
    while que:
        i, c = que.popleft()
        if i == target:
            result.append(c)
        else:
            arr[i] = 1
            if 0 <= i * 2 <= 100000:
                if arr[i*2] == 0:
                    que.append([i * 2, c + 1])
            if 0 <= i + 1 <= 100000:
                if arr[i+1] == 0:
                    que.append([i + 1, c + 1])
            if 0 <= i - 1 <= 100000:
                if arr[i-1] == 0:
                    que.append([i - 1, c + 1])
    return result


N, M = map(int, input().split())

arr = [0] * 100001
c = 0

max_result = cal(N, M, c)

print(min(max_result))
print(max_result.count(min(max_result)))