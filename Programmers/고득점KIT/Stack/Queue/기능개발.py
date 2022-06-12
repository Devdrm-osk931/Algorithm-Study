def solution(progresses, speeds):
    answer = []
    days_needed = []

    for progress, speed in zip(progresses, speeds):
        remained = (100 - progress) // speed if (100 - progress) % speed == 0 else (100 - progress) // speed + 1
        days_needed.append(remained)
    
    front = 0
    for idx in range(len(days_needed)):
        if days_needed[idx] > days_needed[front]:
            answer.append(idx - front)
            front = idx
    
    answer.append(len(days_needed) - front)
        
            
    print(days_needed)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))