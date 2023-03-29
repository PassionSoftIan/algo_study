import sys
sys.stdin = open('1946_new_employee_input.txt')

def check(start):
    global count
    for n in range(start):
        if score_lst[start][1] > score_lst[n][1]:
            return
    count += 1


Test_case = int(input())

for tc in range(1, Test_case+1):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    score_lst = sorted(score, key=lambda x: x[0], reverse=True)
    count = 1
    for i in range(1, N):
        check(i)


    print(count)
    print(score_lst)
    print(score)