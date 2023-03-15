import sys
sys.stdin = open('1149_RGB_distance_input.txt')
from itertools import permutations, combinations
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
R = []
G = []
B = []
for i in range(N):
    R.append(arr[i][0])
    G.append(arr[i][1])
    B.append(arr[i][2])

print(arr)


RGB = []
RGR = []
RBR = []
GRG = []
GBG = []
BGB = []
BRB = []

for i in range(N):
    for j in range(N):
        for n in range(N):
            if i != j and i != n and j != n:
                RGB.append([R[i], G[j], B[n]])
                RGB.append([R[i], G[j], R[n]])
                RGB.append([R[i], B[j], R[n]])
                RGB.append([G[i], R[j], G[n]])
                RGB.append([G[i], B[j], G[n]])
                RGB.append([B[i], G[j], B[n]])
                RGB.append([B[i], R[j], B[n]])

print(RGB)

result_min = sum(RGB[0])
for i in range(1, len(RGB)):
    if result_min > sum(RGB[i]):
        result_min = sum(RGB[i])
        print(RGB[i])

print(result_min)