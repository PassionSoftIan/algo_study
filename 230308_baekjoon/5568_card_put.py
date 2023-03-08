import sys
sys.stdin = open('5568_card_put_input.txt')
from itertools import permutations

N = int(input())
K = int(input())

card = []
for nc in range(N):
    card.append(input())

result = set()
for i in permutations(card, K):
    result.add(''.join(i))
print(len(result))