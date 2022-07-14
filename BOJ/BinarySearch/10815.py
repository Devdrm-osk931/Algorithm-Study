# BOJ_10815_실버5
# check_cards에 있는 카드들이 my_cards에 존재하는지 여부를 확인하는 문제
# 존재한다면 1을 출력하고 존재하지 않는다면 0을 출력한다
# n과 m의 범위가 500,000까지이므로, 일반 선형 탐색은 시간 초과가 발생할 것이므로 이분탐색으로 확인

n = int(input())
my_cards = list(map(int, input().split()))
my_cards.sort()

m = int(input())
check_cards = list(map(int, input().split()))


def binary_search(array, target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


for check_card in check_cards:
    print(1 if binary_search(my_cards, check_card) else 0, end=' ')
