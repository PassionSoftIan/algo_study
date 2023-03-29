import sys
sys.stdin = open('14889_start_and_link_input.txt')


def backtracking1(depth, s):
    if depth == N//2:
        # count_1 = 0
        # for i in range(len(result)//2):
        #     count_1 += arr[i]
        # for j in range(len(result)//2, len(result)):
        print(result)
        return

    for i in range(s, N):
        if visited[i] == 0:
            result[0].append(person[i])
            visited[i] = 1
            backtracking1(depth+1, i)
            visited[i] = 0
            result[0].pop()




N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

person = list(range(1, N+1))

visited = [0] * N

result = [[] for _ in range(2)]

print(person)
print(arr)


backtracking1(0, 0)