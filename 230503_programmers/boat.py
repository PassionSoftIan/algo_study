def solution(peoples, limit):
    answer = 0
    peoples.sort()

    start = 0
    end = len(peoples) - 1
    visited = [0] * len(peoples)

    while True:
        if start > end or start == end:
            if visited[start] == 0 or visited[end] == 0:
                answer += 1
                return answer
            else:
                return answer
        if peoples[start] + peoples[end] <= limit:
            visited[start] = 1
            visited[end] = 1
            start += 1
            end -= 1
            answer += 1
        else:
            visited[end] = 1
            end -= 1
            answer += 1