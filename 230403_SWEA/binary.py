Test_case = int(input())

for tc in range(1, Test_case+1):
    N = int(input())

    octagonal = input()

    binary = ''

    for i in octagonal:
        decimal = int(i, 16)
        binary += format(decimal, 'b').zfill(4)

    max_count = 0
    count = 0
    for i in binary:
        if i == '1':
            count += 1
            if max_count < count:
                max_count = count
        if i == '0':
            count = 0

    print(f'#{tc} {max_count}')