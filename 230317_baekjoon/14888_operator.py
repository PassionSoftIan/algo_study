import sys
sys.stdin = open('14888_operator_input.txt')

N = int(input())

num = list(map(int, input().split()))

operator_lst = list(map(int, input().split()))


max_result = 0
min_result = 0
count = 0

def operator(depth, cal, plus, minus, multiple, divide):
    global max_result
    global min_result
    global count

    if depth == N:
        if count == 0:
            max_result = cal
            min_result = cal
            count += 1
            return
        else:
            if cal >= max_result:
                max_result = cal
            if cal <= min_result:
                min_result = cal
        return

    if plus > 0:
        operator(depth+1, cal + num[depth], plus-1, minus, multiple, divide)

    if minus > 0:
        operator(depth+1, cal - num[depth], plus, minus-1, multiple, divide)

    if multiple > 0:
        operator(depth+1, cal * num[depth], plus, minus, multiple-1, divide)

    if divide > 0:
        operator(depth+1, int(cal / num[depth]), plus, minus, multiple, divide-1)


operator(1, num[0], operator_lst[0], operator_lst[1], operator_lst[2], operator_lst[3])

print(max_result)
print(min_result)