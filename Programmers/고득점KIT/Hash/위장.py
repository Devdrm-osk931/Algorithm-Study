def solution(clothes):
    category = {}
    answer = 1
    for elem in clothes:
        if elem[1] in category:
            category[elem[1]] += 1
        else:
            category[elem[1]] = 1

    product = 1
    for val in category.values():
        product = product * (val + 1)
    answer = product - 1

    return answer
