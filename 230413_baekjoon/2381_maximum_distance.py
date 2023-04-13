import sys
sys.stdin = open('2381_maximum_distance_input.txt')

N = int(input())

lst = set()

coordinate = []

for nc in range(N):
    n, m = map(int, input().split())
    lst.add(n)
    lst.add(m)
    coordinate.append([m, n])

M = max(lst)

edge = [[] for _ in range(M*M+1)]

print(lst)
print(edge)

print(coordinate)