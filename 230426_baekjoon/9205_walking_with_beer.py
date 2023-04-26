import sys
sys.stdin = open('9205_walking_with_beer_input.txt')

Test_case = int(input())

for tc in range(Test_case):
    N = int(input())
    home = list(map(int, input().split()))

    store = []
    for nc in range(N):
        x, y = map(int, input().split())
        store.append([x, y])

    stage = list(map(int, input().split()))

    start = [[home[0], home[1]]]
    visited = [0]*(len(store))

    bit = 0
    while start:
        n, m = start.pop()
        for sg in range(len(store)):
            if visited[sg] == 0:
                if abs(n - store[sg][0]) + abs(m - store[sg][1]) <= 1000:
                    start.append([store[sg][0], store[sg][1]])
                    visited[sg] = 1
        if abs(n - stage[0]) + abs(m - stage[1]) <= 1000:
            print('happy')
            bit = 1
            break

    if bit == 0:
        print('sad')