def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[0])

    camera = routes[0][1]

    for i in range(0, len(routes)):
        if camera < routes[i][0]:
            answer += 1
            camera = routes[i][1]

    return answer