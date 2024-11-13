import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer


from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    tangerine.sort(key = lambda t: (-counter[t], t))
    return len(set(tangerine[:k]))
