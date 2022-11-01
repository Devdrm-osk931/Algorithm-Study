def solution(sx1, sy1, sx2, sy2, sticks):
    def in_range(a, b):
        return sx1 < a < sx2 and sy1 < b < sy2


    answer = 0
    for stick in sticks:
        x1, y1, x2, y2 = stick

        if in_range(x1, y1) and in_range(x2, y2):
            answer += 1

    return answer