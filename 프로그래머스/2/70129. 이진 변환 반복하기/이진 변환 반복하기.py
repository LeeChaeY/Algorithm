# 약 10분 소요
def solution(s):
    answer = [0, 0]
    while s != '1':
        cnt = 0
        answer[0] += 1
        for c in s:
            if c == '1':
                cnt += 1
            else:
                answer[1] += 1
        s = ''
        while cnt > 0:
            s = s + str(cnt%2)
            cnt //= 2
    return answer