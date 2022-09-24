import itertools


def solution(users, emoticons):
    answer = []
    emoticon_cnt = len(emoticons)
    # 10%, 20%, 30%, 40%
    rates = [10, 20, 30, 40]
    cases = itertools.product(rates, repeat = emoticon_cnt)
    max_subscribers = 0
    max_profit = 0

    for case in cases:
        total_subscriber = 0
        total_profit = 0

        # 각 사용자마다 확인한다
        for user in users:
            user_rate = user[0]
            user_limit = user[1]
            user_payed = 0

            # 각 이모티콘의 가격과 이모티콘에 적용되는 할인율
            for emoticon, rate in zip(emoticons, list(case)):
                if rate >= user_rate:
                    discounted_price = emoticon - emoticon * (rate / 100)
                    user_payed += discounted_price

            if user_payed >= user_limit:
                total_subscriber += 1
            else:
                total_profit += user_payed

        if (max_subscribers, max_profit) < (total_subscriber, total_profit):
            max_subscribers = total_subscriber
            max_profit = total_profit

    return [max_subscribers, int(max_profit)]


users = [
    [40, 2900],
    [23, 10000],
    [11, 5200],
    [5, 5900],
    [40, 3100],
    [27, 9200],
    [32, 6900]
]

emoticons = [1300, 1500, 1600, 4900]

print(solution(users, emoticons))
