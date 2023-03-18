import sys
sys.stdin = open('1759_password_making_input.txt')

L, C = map(int, input().split())

word = sorted(list(input().split()))
result = []
visited = [0] * C
vowel = ['a', 'e', 'i', 'o', 'u']

def making(depth, s):
    if depth == L:
        c = 0
        v = 0
        for n in result:
            if n in vowel:
                v += 1
            else:
                c += 1
        if v >= 1 and c >=2:
            print(*result, sep='')
            return



    prev = ''
    for i in range(s, C):
        if visited[i] == 0 and word[i] != prev:
            result.append(word[i])
            visited[i] = 1
            making(depth+1, i)
            visited[i] = 0
            prev = word[i]
            result.pop()


making(0,0)