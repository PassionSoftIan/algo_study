import sys
sys.stdin = open('1182_permutation_sum_input.txt')
from itertools import combinations

N, S = map(int, input().split())

num = list(map(int, input().split()))
num_lst = []
count = 0
for i in range(1, N+1):
    num_lst.append(list(combinations(num, i)))
for n in range(len(num_lst)):
    for m in range(len(num_lst[n])):
        if sum(num_lst[n][m]) == S:
            count += 1
print(count)