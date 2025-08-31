def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    stack = []
    # Map closing --> opening
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in "({[":
            stack.append(char)  # push opening
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False  # mismatch or empty stack
            stack.pop()  # matched pair, pop it

    return not stack  # valid if nothing left
