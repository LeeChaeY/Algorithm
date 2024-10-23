def solution(name, yearning, photo):
    answer = []
    num_d = {}
    for p, y in zip(name, yearning):
        num_d[p] = y
    for ph in photo:
        sum = 0
        for p in ph:
            if p in num_d:
                sum += num_d[p]
        answer.append(sum)
    return answer