import sys
sys.stdin = open('12738_LIS_input.txt')

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * 1000000

for i in range(len(arr)):
