class Solution(object):
    def isValid(self, s):
        par={']':'[','}':'{',')':'('}
        stack=[]
        for ch in s:
            if ch in par.values():
                stack.append(ch)
            elif ch in par:
                if not stack or stack[-1]!=par[ch]:
                    return False
                stack.pop()
        if stack:
            return False
        return True



    
        
        