def solution(today, terms, privacies):
    answer = []
    end_time = [0]
    term_map = dict()
    cnt = 0

    for term in terms:
        term = term.split()
        term_map[term[0]] = int(term[1])


    # privacies 순회
    for privacy in privacies:
        cnt += 1
        privacy = privacy.split(" ")
        intake = privacy[0]
        type = privacy[1]

        year, month, date = list(map(int, intake.split(".")))
        duration = term_map[type]
        month += int(duration)
        date -= 1
        if date == 0:
            date += 28
            month -= 1

        while month > 12:
            month -= 12
            year += 1

        end_time.append(str(year) + "." + str(month) + "." + str(date))

    for i in range(1, len(privacies) + 1):
        today_year, today_month, today_date = list(map(int, today.split(".")))
        end_year, end_month, end_date = list(map(int, end_time[i].split(".")))

        if today_year > end_year:
            answer.append(i)
            continue

        if today_year == end_year:
            if today_month > end_month:
                answer.append(i)
                continue

        if today_year == end_year and today_month == end_month:
            if today_date > end_date:
                answer.append(i)
                continue
    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
solution(today, terms, privacies)