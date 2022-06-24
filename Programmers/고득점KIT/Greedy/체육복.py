# def solution(n, lost, reserve):
#     reserve.sort()
#     answer = n
#     check = {}
#     for stu in lost:
#         if stu in reserve:
#             lost.remove(stu)
#             reserve.remove(stu)
#
#     for student_num in lost:
#         check[student_num] = True
#
#     # print("-----------------")
#     # print("n:", n)
#     # print("lost:", lost)
#     # print("reserve:", reserve)
#     # print("answer:", answer)
#     # print("-----------------")
#
#     for student_num in lost:
#         if 1 <= (student_num - 1) <= n and (student_num - 1) in reserve:
#             reserve.remove((student_num - 1))
#             check[student_num] = False
#
#         elif 1 <= (student_num + 1) <= n and (student_num + 1) in reserve:
#             reserve.remove((student_num + 1))
#             check[student_num] = False
#
#     for value in check.values():
#         if value:
#             answer -= 1
#
#     # print("-----------------")
#     # print("n:", n)
#     # print("lost:", lost)
#     # print("reserve:", reserve)
#     # print("answer:", answer)
#     # print("-----------------")
#
#     return answer
#
#
# # solution(5, [1, 2], [2, 3])

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]

    for r in _reserve:
        left = r - 1
        right = r + 1

        if left in _lost:
            _lost.remove(left)
        elif right in _lost:
            _lost.remove(right)

    return n - len(_lost)
