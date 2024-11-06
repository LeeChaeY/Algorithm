# 약 1시간 소요, 질문하기에서 스택 활용법 봄
def solution(s):
    answer = 1
    s = list(s)
    stack = []
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    return 0 if stack else 1