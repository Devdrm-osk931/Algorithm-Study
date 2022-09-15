def solution(a, b):
    if a <= b:
        left, right = a, b
    else:
        left, right = b, a

    return sum([
        i
        for i in range(left, right + 1)
    ])