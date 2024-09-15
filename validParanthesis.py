class Solution(object):
    def isValid(self, s):
        stack = [] 
        checker = {")": "(", "}":"{", "]":"["}
        for c in s:
            if c in checker:
                if stack and stack[-1] == checker[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        return True if not stack else False