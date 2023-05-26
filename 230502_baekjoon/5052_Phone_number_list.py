import sys
sys.stdin = open('5052_Phone_number_list_input.txt')

Test_case = int(input())

for tc in range(Test_case):
    N = int(input())

    num_lst = []
    for nc in range(N):
        num_lst.append(int(input()))

    print(num_lst)