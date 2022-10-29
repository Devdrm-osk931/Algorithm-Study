def solution(n, records, cart, k):
    buy_sets = []

    for record in records:
        record = set(list(map(int, record.split()))[1:])
        buy_sets.append(record)


    # A를 구매했을 때 B를 구매할 확률
    def getPercentage(A, B):
        # A와 B를 함께 구매한 케이스, A만 구매한 케이스
        together_cnt, a_cnt = 0, 0

        for buy_set in buy_sets:
            if A in buy_set:
                a_cnt += 1
            if A in buy_set and B in buy_set:
                together_cnt += 1

        return together_cnt / a_cnt

    # A를 구매한 빈도수를 구한다
    def getFrequency(A):
        frequency = 0
        for buy_set in buy_sets:
            if A in buy_set:
                frequency += 1
        return frequency


    cart_set = set(cart)
    # 카트에 담긴 물건이 k개가 될 때까지 진행한다
    while len(cart) < k:
        candidates = []
        for candidate in range(1, n + 1):
            if candidate in cart_set:
                continue

            candidate_percentage = 0
            for item in cart:
                candidate_percentage = max(candidate_percentage, getPercentage(item, candidate))

            candidates.append((candidate, candidate_percentage, getFrequency(candidate)))
        candidates.sort(key=lambda x: (-x[1], -x[2], x[0]))
        cart.append(candidates[0][0])
        cart_set.add(candidates[0][0])


    return sorted(cart)