# 주식 이익 최대화하기
import sys


def getMax(prices):
    min_price = sys.maxsize
    max_profit = 0

    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(price - min_price, max_profit)

    return max_profit

def getMaxByTwoPointer(prices):
    buy = 0
    sell = 1
    profit = 0

    while True:
        if len(prices) == sell:
            return profit
        if prices[sell] >= prices[buy]:
            profit = max(profit, prices[sell] - prices[buy])
        else:
            buy = sell
        sell += 1

print(getMaxByTwoPointer([7,1,5,3,6,4,10]))

"""
이익이 일어나기 위해선 적은 값으로 구매하여 큰 값으로 팔아야한다

각 가격값을 순회하며 최저점을 갱신한다
최대 이익값을 계산한다 -> 이전에 계산한 최대 이익값과 현재 가격과 구매 가격(min_price)의 차이
만약 최소 가격이 갱신이 되었다면 이 값은 0이 될것이다 하지만 결국 최저값이 갱신 되었다는 말은 이후 값들과 비교할때 기존 최소값보다 새로운 새로운 값으로 이익을 계산하는것이 무조건 이득
하지만 만약 최소구매값 갱신 이후에 이익이 갱신되지 않는다면 이전에 계산되었던 최대 이익값으 반환되게 된다.
논리적으로 결함이 없는 코드가 된다.
투 포인터와 같은 로직인것 같다.
"""