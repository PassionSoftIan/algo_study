import sys
sys.stdin = open('2477_yellow_melon_input.txt')

N = int(input())

field = [[] for _ in range(7)]

odd_max = 0
odd_max_idx = 0

even_max = 0
even_max_idx = 0

for go in range(1, 7):
    n, m = map(int, input().split())
    field[go].append(m)
    if go % 2 == 0:
        if even_max < m:
            even_max = m
            even_max_idx = go
    else:
        if odd_max < m:
            odd_max = m
            odd_max_idx = go

top = 0
low = 0

if even_max_idx > odd_max_idx:
    top = even_max_idx
    low = odd_max_idx
else:
    top = odd_max_idx
    low = even_max_idx

short_odd = 0
short_even = 0

for i in range(1, 7):
    if i == 1 and top == 6:
        continue
    if low == 1 and i == 6:
        continue
    if i == top or i == low:
        continue
    if i == low-1:
        continue
    if i == top+1:
        continue
    if i == top-1:
        continue
    if i % 2 == 0:
        short_even = field[i][0]
    else:
        short_odd = field[i][0]

area = (odd_max * even_max) - (short_even * short_odd)

print(area*N)