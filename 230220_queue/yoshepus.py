# import sys
from collections import deque
# input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(range(1, N+1))
count = 0
for i in range(len(arr)):
