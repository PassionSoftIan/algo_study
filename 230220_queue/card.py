N = int(input())
arr = list(range(1, N+1))
for i in range(len(arr)-1):
        arr.pop(0)
        arr.append(arr.pop(0))
print(*arr)