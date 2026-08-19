from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        
        reserved_rows = defaultdict(int)
        for r, c in reservedSeats:
            reserved_rows[r] |= (1 << c)
            
        
        ans = (n - len(reserved_rows)) * 2
        
        LEFT_MASK   = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        RIGHT_MASK  = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)
        MIDDLE_MASK = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7) 
        
        for mask in reserved_rows.values():
            left_free = (mask & LEFT_MASK) == 0
            right_free = (mask & RIGHT_MASK) == 0
            mid_free = (mask & MIDDLE_MASK) == 0
            
            if left_free and right_free:
                ans += 2
            elif left_free or right_free or mid_free:
                ans += 1
                
        return ans