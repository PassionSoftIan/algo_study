import sys
sys.stdin = open('1158_yosepus_input.txt')
from collections import deque

N, K = map(int, input().split())

person = deque(list(range(1, N+1)))

result = []
count = 0
while person:
    for i in range(len(person)):
        A = person.popleft()
        count += 1
        if count == K:
            result.append(str(A))
            count = 0
        else:
            person.append(str(A))

print('<', ', '.join(result), '>', sep='')