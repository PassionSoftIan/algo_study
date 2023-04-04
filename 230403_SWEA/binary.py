import sys
sys.stdin = open('binary_input.txt')

Test_case = int(input())

for tc in range(1, Test_case+1):
    N, num = input().split()

    bi = ''
    for i in num:
        bi += format(int(i, 16), 'b').zfill(4)

    print(f'#{tc} {bi}')