import sys
sys.stdin = open('20364_real_estate_struggle_input.txt')

N, Q = map(int, input().split())

want = [0]
for dck in range(Q):
    want.append(int(input()))

real_estate = [[] for _ in range(N+1)]

result = []

land = 0
for duck in range(1, len(want)):
    count = 0
    land = want[duck]
    while 3 < land:
        land = round(land/2, 3)
    while land < len(real_estate):
        if real_estate[int(land)]:
            count = int(land)
            break
        land = round(land * 2, 3)
    if count == 0:
        real_estate[want[duck]].append(duck)
        result.append(0)
    else:
        result.append(count)
print(re)
for i in result:
    print(i)



# for duck in range(1, len(want)):
#     if want[duck] % 2 == 0:
#         if want[duck] % 3 == 0:
#             for find in range(len(want)//2):
#                 if real_estate[3*(2**find)]:
#                     result.append(real_estate[find*2][0])
#                 else:
#                     result.append(0)
#                     real_estate[find*2].append(want[duck])
#         else:
#             for find in range(len(want)//2):
#                 if real_estate[2*(2**find)]:
#     else:
#         for find in range(len(want)//2):
#             if real_estate[2*(2**find)+1]
#
#         real_estate[want[duck]].append(duck)
#
# print(real_estate)





# for i in range(1, len(want)):
#     if not real_estate[i]:
#         result.append(0)
#
#     else:
#         if real_estate[i][0] < want[i]:
#             if want[i] % 2 == 0:
#                 for z in range(1, len(real_estate)//2):
#                     if real_estate[2**z]:
#                         result.append(real_estate[z][0])
#                         break
#             else:
#                 for z in range(1, len(real_estate)//2):
#                     if real_estate[2**z+1]:
#                         result.append(real_estate[z][0])
#                         break
#     real_estate[i].append(want[i])
#     real_estate[want[i]].append(i)
#
# print(want)
# print(real_estate)
# print(result)
# for i in result:
#     print(i)