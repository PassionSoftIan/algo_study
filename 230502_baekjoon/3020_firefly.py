import sys
sys.stdin = open('3020_firefly_input.txt')


def binary_search(start, end, chk, bit):
    while start <= end:
        mid = (start + end) // 2
        if stalagmite[mid] <= chk:
            start = mid + 1
        else:
            end = mid - 1

    if bit == 0:
        chk += 0.5
        visited[int(chk)] += start
    else:
        chk -= 0.5
        visited[int(chk)] += start


N, H = map(int, input().split())

stalagmite = []
stalactite = []

visited = [0] * (N+1)

for st in range(N):
    if st % 2 == 0:
        stalagmite.append(int(input()))
    else:
        stalactite.append(int(input()))
# -------------------
stalagmite.sort()

start_mite = 0
end_mite = len(stalagmite) - 1
# -------------------

# -------------------
stalactite.sort()

start_tite = 0
end_tite = len(stalactite) - 1
# -------------------
for check in range(1, N+1):
    binary_search(start_mite, end_tite, check - 0.5, 0)
    binary_search(start_tite, end_tite, H - check + 0.5, 1)

print(stalagmite)
print(stalactite)

print(visited)