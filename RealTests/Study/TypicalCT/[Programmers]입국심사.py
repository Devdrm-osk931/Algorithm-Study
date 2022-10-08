def solution(n, times):
    times = sorted(times)

    left = times[0]
    right = times[-1] * n

    while left <= right:
        mid = (left + right) // 2
        possible = 0
        # mid 시간동안 n명 검사가 가능한가?
        for time in times:
            possible += mid//time

        if possible >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

print(solution(6, [7, 10]))