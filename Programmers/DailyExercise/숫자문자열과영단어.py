# Programmers
# 2021 카카오 인턴 채용

number_to_string_mapper = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def solution(s):
    answer = ""
    check = ""

    for char in s:
        if not char.isdigit():
            check += char
            if check in number_to_string_mapper:
                answer += str(number_to_string_mapper[check])
                check = ""
        else:
            answer += char

    return int(answer)

