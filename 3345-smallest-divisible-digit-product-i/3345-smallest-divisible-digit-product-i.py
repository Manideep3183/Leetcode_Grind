class Solution(object):
    def smallestNumber(self, n, t):
        
        def get_digit_product(num):
            prod = 1
            for digit in str(num):
                prod *= int(digit)
            return prod

        while True:
            if get_digit_product(n) % t == 0:
                return n
            n += 1