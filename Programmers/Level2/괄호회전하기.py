# Programmers
# 괄호회전하기 Lv2

from collections import deque


def possible(s):
    stack = []
    for elem in s:
        if elem in ["[", "(", "{"]:
            stack.append(elem)
        elif elem == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False

        elif elem == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False

        else:
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


def solution(s):
    answer = 0
    s = deque(s)

    for cnt in range(len(s)):
        s.rotate(-1)
        if possible("".join(list(s))):
            answer += 1
    return answer