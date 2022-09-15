def solution(a, b):
    dict = {
        0: "SUN",
        1: "MON",
        2: "TUE",
        3: "WED",
        4: "THU",
        5: "FRI",
        6: "SAT"
    }
    date = 4
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for month in range(a - 1):
        day = days[month]
        date = (date + day) % 7

    date = (date + b) % 7

    return dict[date]

print(solution(5, 24))