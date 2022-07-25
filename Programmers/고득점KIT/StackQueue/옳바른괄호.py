def solution(s):
    answer = True
    stack = []
    
    for elem in s:
        if elem == "(":
            stack.append(elem)
        else:
            if not stack:
                return False
            stack.pop()
    
    if stack:
        return False


    return True