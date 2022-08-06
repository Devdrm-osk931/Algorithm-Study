def solution(tasks):
    task_cnt = {}

    for task in tasks:
        if task not in task_cnt:
            task_cnt[task] = 1
        else:
            task_cnt[task] += 1
    
    cnt = 0
    for _, val in task_cnt.items():
        # 특정 작업이 한 개만 있는 경우에는 수행할 수 없으므로 -1을 리턴한다
        if val == 1:
            return -1
        
        # val 값을 최대한 3개씩 묶어서 진행한다
        group3 = val // 3
        remainder = val % 3

        # 만약 나머지가 짝수라면
        if remainder % 2 == 0:
            group2 = remainder // 2
        else:
            group3 -= 1
            group2 = (remainder + 3) // 2
        
        cnt += group3 + group2


    return cnt

print(solution([1,1,2,3,3,2,2]))  #3
print(solution([4,1,1,1,1,2,3]))  #-1
print(solution([1,1,2,2]))  #2