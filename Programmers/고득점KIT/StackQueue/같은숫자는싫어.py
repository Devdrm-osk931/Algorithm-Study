def solution(arr):
    answer = []
    
    prev_num = -1

    for elem in arr:
        if elem == prev_num:
            continue
        prev_num = elem
        answer.append(prev_num)
    return answer

print(solution([1,1,3,3,0,1,1]	))