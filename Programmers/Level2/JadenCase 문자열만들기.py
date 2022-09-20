def solution(s):
    answer = ''
    words = list(s.split(" "))
    for word in words:
        word = list(word)
        for idx in range(len(word)):
            if idx == 0:
                if word[idx].isalpha():
                    word[idx] = word[idx].upper()
                else:
                    continue

            else:
                if word[idx].isalpha():
                    word[idx] = word[idx].lower()
                else:
                    continue

        answer = answer + "".join(word) + " "

    return answer[:-1]

print(solution("for the last week"))