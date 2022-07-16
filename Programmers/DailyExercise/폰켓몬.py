def solution(nums):
    n = len(nums)

    if len(set(nums)) >= n/2:
        answer = n/2
    else:
        answer = len(set(nums))

    return int(answer)
