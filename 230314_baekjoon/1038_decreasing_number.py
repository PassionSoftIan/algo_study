import sys
sys.stdin = open('1038_decreasing_number_input.txt')

N = int(input())
num = []
count = -1
for n in range(1000001):
    num.append(list(map(str, str(n))))

for i in range(len(num)):
    if len(num[i]) == 1:
        count += 1
        if count == N:
            print(*num[i])
            break
    else:
        for j in range(len(num[i]) - 1):
            if num[i][j] > num[i][j + 1]:
                count += 1
                if count == N:
                    print(*num[i])