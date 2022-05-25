def solution(phone_book):
    answer = True

    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
            answer = False
            return answer

    return answer


tests = [
    ["119", "97674223", "1195524421"],
    ["123","456","789"],
    ["12","123","1235","567","88"],
    ["12", "456", "1234"]
]

for test in tests:
    print(solution(test))
'''

# 효율성 테스트 통과 X
# 채점 결과
# 정확성: 83.3
# 효율성: 8.3
# 합계: 91.7 / 100.0

def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        base = phone_book[i]
        for j in range(i + 1, len(phone_book)):
            if base == phone_book[j][:len(base)]:
                answer = False
                return answer
    return answer

'''