'''
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
'''


def solution(participant, completion):
    check = dict()

    for person in participant:
        if person in check:
            check[person] += 1

        else:
            check[person] = 1

    for completed in completion:
        check[completed] -= 1

    for key, value in check.items():
        if value > 0:
            return key