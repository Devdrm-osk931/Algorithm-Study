prime_set = set()

def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def make_permutation(result, others):
    if result != "":
        if is_prime(int(result)):
            prime_set.add(int(result))
            print(int(result))

    for i in range(len(others)):
        make_permutation(result + others[i], others[:i] + others[i+1:])

def solution(numbers):
    answer = 0
    numbers_list = list(numbers)
    make_permutation("", numbers_list)

    print(prime_set)
    answer = len(prime_set)
    return answer