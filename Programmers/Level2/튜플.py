# Programmers
# 튜플 Lv2 카카오 인턴 기출

def solution(s):
    answer_set = set()
    answer = []

    s = s[1:-1].replace("{", "/").replace("}", "/").replace("/,/", "/")[1:-1].split("/")
    s.sort(key=lambda x: len(x))

    for elem in s:
        for num in elem.split(","):
            if num not in answer_set:
                answer_set.add(num)
                answer.append(int(num))
            else:
                continue
    return answer