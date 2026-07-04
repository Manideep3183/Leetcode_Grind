class Solution(object):
    def isValid(self, s):
        pairs = { '(':')','{':'}','[':']'}
        stack = []
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            elif ch in pairs.values():
                if not stack or pairs[stack[-1]] != ch:
                    return False
                stack.pop()
        if stack:
            return False
        return True
                    

        