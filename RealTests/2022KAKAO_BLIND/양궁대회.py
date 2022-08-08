from itertools import product


def solution(n, info):
    answer = []
    target_scores = [i for i in range(11)]
    ryan_scores = product(target_scores, repeat=n)
    for ryan_score in ryan_scores:
        print(ryan_score)
    return answer


solution(2, [2,1,1,1,0,0,0,0,0,0,0])