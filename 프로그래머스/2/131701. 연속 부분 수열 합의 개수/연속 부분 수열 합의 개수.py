# 15분 소요
def solution(elements):
    # ans = elements+ [sum(elements)]
    ans = set(elements+[sum(elements)])
    size = len(elements)
    elements *= 2
    for i in range(2, size):
        for j in range(size):
            ans.add(sum(elements[j:j+i]))
    return len(ans)
