def solution(birthdays):
    answer = 0

    days_map = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    num_to_day_map = {
        0: "SUN",
        1: "MON",
        2: "TUE",
        3: "WED",
        4: "THU",
        5: "FRI",
        6: "SAT"
    }

    # 정렬
    birthdays = sorted(birthdays)

    # 총 사람 수
    people_cnt = len(birthdays)

    # 각 사람의 날짜(일 기준), 요일을 구한다
    people_map = dict()

    for i in range(people_cnt):
        birthday = birthdays[i]
        month = birthday[0:2]
        day = birthday[2:]

        total_day = 0

        for m in range(1, int(month)):
            total_day += days_map[m]
        total_day += int(day)

        yoil = num_to_day_map[(total_day - 1) % 7]

        people_map[i] = [total_day, yoil]


    # 각 사람마다 확인
    # for give in range(people_cnt):
    #     for to in range(people_cnt):
    #         # 자신에게 선물을 주지 않는다
    #         if give == to:
    #             continue

    #         # 상대방과 생일이 5일 미만으로 차이가 나거나, 생일이 토요일/일요일인 경우 선물을 주지 않는다
    #         if abs(people_map[give][0] - people_map[to][0]) < 5 or people_map[to][1] == "SAT" or people_map[to][1] == "SUN":
    #             continue

    #         else:
    #             answer += 1


    # 위 코드를 아주 미세하게 개선
    for i in range(people_cnt):
        for j in range(i + 1, people_cnt):
            # 상대방과 생일이 5일 미만으로 차이가 나거나, 생일이 토요일/일요일인 경우 선물을 주지 않는다
            if abs(people_map[i][0] - people_map[j][0]) < 5:
                continue

            # 평 평/ /주 평/
            if people_map[j][1] == "SAT" or people_map[j][1] == "SUN":
                # 주말 주말
                if people_map[i][1] == "SAT" or people_map[i][1] == "SUN":
                    continue
                # 평일 주말
                else:
                    answer += 1

            else:
                # 주말 평일
                if people_map[i][1] == "SAT" or people_map[i][1] == "SUN":
                    answer += 1
                # 평일 평일
                else:
                    answer += 2
    return answer