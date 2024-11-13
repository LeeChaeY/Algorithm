# 약 25분 소요
def solution(k, tangerine):
    answer = 0
    d = {i:0 for i in tangerine}
    for i in tangerine:
        d[i] += 1
    d = sorted(d.items(), key=lambda d:d[1], reverse=True)
    sum = 0
    for key, v in d:
        answer += 1
        sum += v
        if sum >= k:
            break
    return answer