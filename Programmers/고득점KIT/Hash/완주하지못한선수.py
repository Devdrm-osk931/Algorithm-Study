# Programmers_완주하지 못한 선수_Level 2
##
def solution(participant, completion):
    answer = ''
    
    done = {}

    for c_person in completion:
        # add people who completed to done dictionary
        if c_person in done:
            done[c_person] += 1
        else:
            done[c_person] = 1
    
    for person in participant:
        if person in done:
            done[person] -= 1
            if not done[person]:
                del(done[person])
        else:
            answer = person
                
                
    return answer