import sys
sys.stdin = open('1208_flatten_input.txt')

for tc in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))
    for i in range(N):
        for j in range(len(box)):
            if box[j] == max(box):
                A = box.pop(j)
                box.append(A - 1)
                break
        for k in range(len(box)):
            if box[k] == min(box):
                B = box.pop(k)
                box.append(B + 1)
                break

    print(f'#{tc} {max(box) - min(box)}')