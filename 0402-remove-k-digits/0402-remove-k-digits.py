class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        if len(num) == k:
            return '0'

        for d in num:
            while stack and k > 0 and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
            
        # for sorted number
        if k > 0:
            stack = stack[:-k]

        result = ''.join(stack).lstrip('0')
        return result if result else '0'
           
        
