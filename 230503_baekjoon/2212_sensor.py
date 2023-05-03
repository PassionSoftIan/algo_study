import sys
sys.stdin = open('2212_sensor_input.txt')

N = int(input())
K = int(input())

sensor = list(map(int, input().split()))
sensor.sort()

distance = []

for i in range(N-1):
    distance.append(sensor[i+1] - sensor[i])

distance.sort()

if distance:
    for i in range(K-1):
        distance.pop()

print(sum(distance))