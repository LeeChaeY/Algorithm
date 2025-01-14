# 5분 정도 소요
def solution(n):
    answer = 1+n if n > 1 else n
    for i in range(2, n):
        if n % i == 0:
            answer += i
    return answer
