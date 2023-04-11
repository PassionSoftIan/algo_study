import sys
sys.stdin = open('2477_yellow_melon_input.txt')

N = int(input())

field = [[] for _ in range(5)]

wide = []
short = []

for node in range(6):
    n, m = map(int, input().split())
    field[n].append(m)

for search in range(1, 5):
    if len(field[search]) == 1:
        wide.append(*field[search])
    else:
        short.append(field[search])

print(wide)
print(short)






print(field)