class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                while stack and abs(ast) > stack[-1] and stack[-1] > 0:
                    stack.pop()
                if stack and stack[-1] == abs(ast):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(ast)
        return stack

                
            
        