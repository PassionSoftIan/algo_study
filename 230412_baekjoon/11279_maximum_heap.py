import sys
sys.stdin = open('11279_maximum_heap_input.txt')
from heapq import heappop, heappush

N = int(input())

heap = []

for i in range(N):
    m = int(input())
    if m == 0 and not heap:
        print(0)
        continue
    if m == 0:
        print(-1 * heappop(heap))
    if m != 0:
        heappush(heap, -1 * m)