def solution(nums):
    n = len(nums)

    if len(set(nums)) >= n/2:
        answer = n/2
    else:
        answer = len(set(nums))

    return int(answer)

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
