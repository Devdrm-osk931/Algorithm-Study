from math import dist


def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    answer = []
    check = {}

    concat = [[steps_one, names_one], [steps_two, names_two], [steps_three, names_three]]
    
    # 각 날짜에 중복된 기록이 있는지 확인할 필요가 있다
    for steps, names, in concat:
        name_dist_dict = {}

        for step, name in zip(steps, names):
            if name not in name_dist_dict:
                name_dist_dict[name] = step
            else:
                name_dist_dict[name] = max(name_dist_dict[name], step)
        
        for name, dist in name_dist_dict.items():
            if name in check:
                check[name] += dist
            else:
                check[name] = dist
    
    for key, value in check.items():
        answer.append((key, value))
    answer.sort(key=lambda x:(-x[1], x[0]))
    returnanswer = []
    for person in answer:
        returnanswer.append(person[0])

    return returnanswer

solution(
[1, 2, 3], ["james", "bob", "alice"], [10, 20, 30], ["james", "alice", "bob"], [1000, 1, 1], ["bob", "alice", "james"])

print()
solution([0, 5, 1], ["evan", "ed", "evan"], [9999], ["rose"], [1], ["richard"])