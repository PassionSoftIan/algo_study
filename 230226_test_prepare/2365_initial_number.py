import sys
sys.stdin = open('2365_initial_number_input.txt')

N = int(input())
max_result = []
max_count = 0
count = 0
result = []
q = []
for i in range(0, N+1):
    q.append(N)
    result.append(N)
    count += 1
    q.append(N-i)
    while q:
        A = q.pop(0)
        B = q.pop(0)
        result.append(B)
        count += 1
        q.append(B)
        if A - B >= 0:
            q.append(A - B)
        else:
            if max_count < count:
                max_count = count
                max_result = result
                result = []
                count = 0
                q.pop(0)
                break
            else:
                result = []
                count = 0
                q.pop(0)
                break
print(max_count)
print(*max_result)