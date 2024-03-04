class Solution:
    def isValid(self, s: str) -> bool:
        L = ['(', '{', '[']
        R = [')', '}', ']'] 

        stack = []

        for c in s:
            if c in L:
                stack.append(c)
            if c in R:
                if not stack or c != R[L.index(stack.pop())]:
                    return False

        if not stack:
            return True
        return False