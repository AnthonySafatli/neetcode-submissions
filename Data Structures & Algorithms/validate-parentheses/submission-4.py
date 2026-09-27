class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        try:
            for c in s:
                if c == ')':
                    if stack.pop() != '(':
                        return False
                elif c == '}':
                    if stack.pop() != '{':
                        return False
                elif c == ']':
                    if stack.pop() != '[':
                        return False
                else:
                    stack.append(c)
        except:
            return False

        return len(stack) == 0
        