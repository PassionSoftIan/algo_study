import sys
sys.stdin = open('14712_nemmonemmo_input.txt')

def backtracking(depth, n, start):
    global count
    if depth == n:
        count += 1
        print(result)
        return

    for i in range(start, N*M):
        if visited[i] == 0:
            visited[i] = 1
            result.append(num[i])
            backtracking(depth + 1, n, i)
            visited[i] = 0
            result.pop()


N, M = map(int, input().split())

num = list(range(1, N*M+1))
visited = [0] * (N*M)
result = []
count = 0

for n in range(N*M+1):
    backtracking(0, n, 0)

print(count)

print((2**(N*M) - ((N-1)*(M-1) * (2**(N*M-4))) - 1))