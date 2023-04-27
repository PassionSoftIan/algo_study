def solution(fees, records):
    answer = []
    temp = []

    temp_in = []
    temp_out = []

    for i in records:
        temp.append(i.split())

    for i in temp:
        if 'IN' in i:
            n, m = i[0].split(':')
            z = int(n) * 60 + int(m)
            temp_in.append([z, int(i[1]), i[2]])
        else:
            n, m = i[0].split(':')
            z = int(n) * 60 + int(m)
            temp_out.append([z, int(i[1]), i[2]])
    temp_in.sort(key=lambda x: (x[1], x[0]))
    temp_out.sort(key=lambda x: (x[1], x[0]))

    info = [0] * 9999
    info_fee = [0] * 9999

    numbers = []

    visited = [0] * len(temp_out)

    while temp_in:
        bit = 0
        time, number, way = temp_in.pop(0)
        if number not in numbers:
            numbers.append(number)
        for j in range(len(temp_out)):
            if number == temp_out[j][1]:
                if visited[j] == 0:
                    bit = 1
                    visited[j] = 1
                    check = temp_out[j][0] - time
                    info[number] += check
                    break

        if bit == 0:
            check = 1439 - time
            info[number] += check

    for i in numbers:
        check = info[i]
        if check <= fees[0]:
            if fees[1] == 0:
                info_fee[i] += -1
            else:
                info_fee[i] += fees[1]

        else:
            if 0 < ((check - fees[0]) / fees[2]) - int((check - fees[0]) / fees[2]) < 1:
                info_fee[i] += (int((check - fees[0]) / fees[2]) + 1) * fees[3] + fees[1]

            else:
                info_fee[i] += int(((check - fees[0]) / fees[2]) * fees[3] + fees[1])

    for i in info_fee:
        if i != 0:
            if i == -1:
                answer.append(0)
            else:
                answer.append(i)

    return answer