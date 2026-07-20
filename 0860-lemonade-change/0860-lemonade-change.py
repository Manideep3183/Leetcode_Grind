class Solution(object):
    def lemonadeChange(self, bills):
        f = 0 
        t = 0
        for bill in bills:
            if bill == 5:
                f += 1
            elif bill == 10:
                if f :
                    t += 1
                    f -= 1
                else:
                    return False
            else:
                if f and t:
                    t -= 1
                    f -= 1
                elif f >= 3:
                    f -= 3
                else :
                    return False      
        return True