import sys
sys.stdin = open('printer_queue_input.txt')
from collections import deque
input = sys.stdin.readline

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    arr = deque(enumerate(list(map(int, input().split()))))
    priority = list(arr)
    count = 0
    while max(arr, key=lambda x: x[1]) != priority[M]:
        while max(arr, key=lambda x: x[1]) != arr[0]:
            for i in range(N):
                if arr[0][1] < priority[i][1]:
                    arr.append(arr.popleft())
        arr.popleft()
        count += 1
    count += 1
    print(count)

test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    docs = deque(list(map(int, input().split())))
    idx = deque(range(n))
    count = 0

    while docs:
        if docs[0] == max(docs):
            cnt += 1
            docs.popleft()
            if idx.popleft() == m:
                break
        else:
            docs.append(docs.popleft())
            idx.append(idx.popleft())
    print(count)