def solution(N, stages):
    answer = []
    
    stage_people_map = {}
    
    for stage in stages:
        if stage not in stage_people_map:
            stage_people_map[stage] = 1
        else:
            stage_people_map[stage] += 1
    
    failure = {}

    for stage in sorted(stage_people_map.keys()):
        print(stage)
        
    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])