# BOJ_10610_30_실버4

def check_if_possible(n):
    # 3의 배수인가?
    if int(n) % 3 != 0:
        return False

    # 0이 존재해야 함
    for digit in n:
        if digit == '0':
            return True
    return False


n = input()

# 30의 배수가 만들어질 수 있는지 확인해본다
possible = check_if_possible(n)
# 가능하지 않다면 -1을 출력한다
if not possible:
    print(-1)
# 가능하다면 숫자를 재배열한다
else:
    n = list(map(str, list(n)))
    n.sort(reverse=True)
    print("".join(n))
