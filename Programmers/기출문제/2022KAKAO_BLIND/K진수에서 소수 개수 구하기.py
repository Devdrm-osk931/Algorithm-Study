# 10진수 숫자 n을 k진수로 변환한다
def radix_transform(n, k):
    result = []

    while n >= k:
        result.append(n % k)
        n //= k
    result.append(n)

    return "".join(map(str, (result[::-1])))

def is_prime(n):
    for divisor in range(2, int(n ** (1/2)) + 1):
        if n % divisor == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    # 주어진 숫자 n을 k진수로 변환한다
    k_num = radix_transform(n, k)
    candidates = [
        i for i in k_num.split("0")
        if i != "1"
    ]
    print(candidates)

    for num in candidates:
        if num != "" and is_prime(int(num)):
            # print(num)
            answer += 1


    return answer

print(solution(437674, 3))
print(solution(110011, 10))
