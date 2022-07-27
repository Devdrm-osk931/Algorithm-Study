import sys
def solution(routes):
    answer = 0
    start, end = sys.maxsize, -sys.maxsize

    for in_time, out_time in routes:
        start = min(start, in_time)
        end = max(end, out_time)

    OFFSET = abs(start)
    N = end - start + 1

    check = [0] * N

    for in_time, out_time in routes:
        for time in range(in_time + OFFSET, out_time + OFFSET + 1):
            check[time] += 1
    print(check)
    return answer

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])