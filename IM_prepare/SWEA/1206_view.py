import sys
sys.stdin = open('1206_view_input.txt')

for tc in range(1, 11):
    N = int(input())
    M = list(map(int, input().split()))

    result = []
    count = 0
    for i in range(2, N-2):
        if M[i] > M[i-1] and M[i] > M[i-2] and \
                M[i] > M[i+1] and M[i] > M[i+2]:
            result.append(M[i-1])
            result.append(M[i-2])
            result.append(M[i+1])
            result.append(M[i+2])
            count += M[i] - max(result)
            while result:
                result.pop()
    print(f'#{tc} {count}')