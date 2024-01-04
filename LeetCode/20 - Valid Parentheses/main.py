def isValid(s: str) -> bool:
    stack = []
    for bracket in s:
        if bracket in '({[':
            stack.append(bracket)
        else:
            if stack == [] \
                or (bracket == ')' and stack[-1] != '(') \
                or (bracket == '}' and stack[-1] != '{') \
                or (bracket == ']' and stack[-1] != '[') :
                return False
            stack.pop()
    return not stack

print(isValid("(}"))