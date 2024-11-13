# 약 40분 소요
def is_collect(s):
    stack = []
    d = {']':'[', '}':'{', ')':'('}
    for c in s:
        if c in d.values():
            stack.append(c)
        elif not stack:
            return 0
        elif d[c] == stack[-1]:
            stack.pop()
    return 1 if not stack else 0

def solution(s):
    answer = is_collect(s)
    for i in range(1, len(s)):
        answer += is_collect(s[i:]+s[:i])
    return answer