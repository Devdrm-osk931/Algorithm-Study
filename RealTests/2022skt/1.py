def solution(logs, events):
    answer = []
    user_log_dict = dict()

    for log in logs:
        time, user, step = log.split()
        if user not in user_log_dict:
            user_log_dict[user] = [step]
        else:
            user_log_dict[user].append(step)

    for user, steps in user_log_dict.items():
        if len(steps) > len(events):
            answer.append(user)
        elif len(steps) == len(events):
            if steps != events:
                answer.append(user)
        else:
            k = len(steps)
            if steps != events[:k]:
                answer.append(user)

    if not answer:
        answer.append("-1")
    return sorted(answer)