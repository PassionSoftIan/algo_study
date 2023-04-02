import sys
sys.stdin = open('4366_bank_duty_input.txt')
Test_case = int(input())

for tc in range(1, Test_case+1):
    binary_lst = list(input())
    ternary_lst = list(input())


    changed_binary = []
    changed_ternary = []

    for i in range(1, len(binary_lst)):
        if binary_lst[i] == '0':
            binary_lst[i] = '1'
            changed_binary.append(int(''.join(binary_lst), 2))
            binary_lst[i] = '0'

        elif binary_lst[i] == '1':
            binary_lst[i] = '0'
            changed_binary.append(int(''.join(binary_lst), 2))
            binary_lst[i] = '1'

    for i in range(1, len(ternary_lst)):
        if ternary_lst[i] == '0':
            ternary_lst[i] = '1'
            changed_ternary.append(int(''.join(ternary_lst), 3))
            ternary_lst[i] = '2'
            changed_ternary.append(int(''.join(ternary_lst), 3))
            ternary_lst[i] = '0'

        elif ternary_lst[i] == '1':
            ternary_lst[i] = '2'
            changed_ternary.append(int(''.join(ternary_lst), 3))
            ternary_lst[i] = '0'
            changed_ternary.append(int(''.join(ternary_lst), 3))
            ternary_lst[i] = '1'

        elif ternary_lst[i] == '2':
            ternary_lst[i] = '1'
            changed_ternary.append(int(''.join(ternary_lst), 3))
            ternary_lst[i] = '0'
            changed_ternary.append(int(''.join(ternary_lst), 3))
            ternary_lst[i] = '2'

    if ternary_lst[0] == '1':
        ternary_lst[0] = '2'
        changed_ternary.append(int(''.join(ternary_lst), 3))

    else:
        ternary_lst[0] = '1'
        changed_ternary.append(int(''.join(ternary_lst), 3))
    # print(changed_ternary)
    # print(changed_binary)

    for i in changed_ternary:
        if i in changed_binary:
            print(f'#{tc} {i}')
            break






    # for i in range(0, len(ternary_lst)):
    #     if ternary_lst[i] == '0':
    #         for j in range(len(ternary_lst)):
    #             changed_ternary[i].append(ternary_lst[j])
    #         changed_ternary[i][i] = '1'
    #         for j in range(len(ternary_lst)):
    #             changed_ternary[i+1].append(ternary_lst[j])
    #         changed_ternary[i+1][i] = '2'
    #
    #     elif ternary_lst[i] == '1':
    #         for j in range(len(ternary_lst)):
    #             changed_ternary[i].append(ternary_lst[j])
    #         changed_ternary[i][i] = '0'
    #         for j in range(len(ternary_lst)):
    #             changed_ternary[i+1].append(ternary_lst[j])
    #         changed_ternary[i+1][i] = '2'
    #
    #     else:
    #         for j in range(len(ternary_lst)):
    #             changed_ternary[i].append(ternary_lst[j])
    #         changed_ternary[i][i] = '1'
    #         for j in range(len(ternary_lst)):
    #             changed_ternary[i+1].append(ternary_lst[j])
    #         changed_ternary[i+1][i] = '0'

    # print(binary_lst)
    # print(ternary_lst)
    # print(changed_binary)
    # print(changed_ternary)







# def backtracking_binary(depth):
#     if depth == len(binary):
#         binary_real = ''
#         for i in result_binary:
#             binary_real += i
#         print(int(binary_real, 2))
#         return
#
#     for i in range(len(binary)):
#         result_binary.append(binary[i])
#         backtracking_binary(depth+1)
#         result_binary.pop()
#
# def backtracking_ternary(depth):
#     if depth == len(ternary):
#         ternary_real = ''
#         for i in result_ternary:
#             ternary_real += i
#         print('----')
#         print(result_ternary)
#         print(int(ternary_real, 3))
#         return
#
#     for i in range(len(ternary)):
#         result_ternary.append(ternary[i])
#         backtracking_ternary(depth+1)
#         result_ternary.pop()
#
# Test_case = int(input())
#
# for tc in range(1, Test_case+1):
#     binary = list(map(str, input()))
#     ternary = list(map(str, input()))
#     visited_binary = [0] * len(binary)
#     visited_ternary = [0] * len(ternary)
#     result_binary = []
#     result_ternary = []
#
#     backtracking_binary(0)
#     backtracking_ternary(0)
#
#
#
#
#     print(ternary, binary)