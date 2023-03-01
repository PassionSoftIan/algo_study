import sys
sys.stdin = open('contact_input.txt')

for tc in range(1, 11):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    arr = [[] for _ in range(101)]
    visited = [0] * (101)
    visited[M] = 1
    stack = [M]
    result = []
    for i in range(N//2):
        arr[num[i*2]].append(num[i*2+1])
    while stack:
        node = stack.pop(0)
        for i in range(len(arr[node])):
            if not visited[arr[node][i]]:
                stack.append(arr[node][i])
                visited[arr[node][i]] = visited[node] + 1

    max_result = 0
    idx = 0
    for i in range(101):
        if max_result <= visited[i]:
            max_result = visited[i]
            idx = i
    print(f'#{tc} {idx}')