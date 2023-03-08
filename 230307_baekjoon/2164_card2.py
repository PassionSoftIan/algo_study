import sys
sys.stdin = open('2164_card2_input.txt')
from collections import deque

input = sys.stdin.readline

N = int(input())

card = deque(list(range(1, N+1)))

while len(card) != 1:
    card.popleft()
    card.append(card.popleft())

print(*card)