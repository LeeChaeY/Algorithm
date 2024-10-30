def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])


def getMinSum(A,B):
    return sum(map(lambda a,b : a*b, sorted(A), sorted(B, reverse=True)))


