import sys
sys.stdin = open('1374_classroom_input.txt')
from collections import deque


N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[2])

queue = deque([0])

count = N

for j in range(1, N):
    bit = 0
    while queue and arr[queue[0]][2] <= arr[j][1]:
        queue.popleft()
        queue.appendleft(j)
        count -= 1
        bit = 1
        break
    if bit == 0:
        queue.append(j)

print(arr)
print(count)


'''
2 14, 15 21

3 8, 12 18

6 27

6 20, 20 25

7 13






1 3, 7 8, 9 10

2 5, 7 11

4 12,
'''