import sys
sys.stdin = open('binary_input.txt')

Test_case = int(input())

for tc in range(1, Test_case+1):
    N = int(input())
    hexadecimal = input()

    decimal = format(int(hexadecimal, 16), 'b')

    max_count = 0
    count = 0
    for i in str(decimal):
        if i == '1':
            count += 1
            if max_count < count:
                max_count = count
        if i == '0':
            count = 0

    print(f'#{tc} {max_count}')