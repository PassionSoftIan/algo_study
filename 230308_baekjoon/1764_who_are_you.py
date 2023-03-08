import sys
sys.stdin = open('1764_who_are_you_input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

who = set()
for i in range(N):
    who.add(input())

you = set()
for j in range(N, N+M):
    you.add(input())

who_are_you = list(sorted(who & you))

print(len(who_are_you))
for i in who_are_you:
    print(i, end='')