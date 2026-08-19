from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Map each row to a bitmask of reserved seats (bits 1 to 10)
        reserved_rows = defaultdict(int)
        for r, c in reservedSeats:
            reserved_rows[r] |= (1 << c)
            
        # Start by assuming every empty row gets 2 groups
        ans = (n - len(reserved_rows)) * 2
        
        # Bitmasks for seat blocks
        LEFT_MASK   = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5) # 0b0000111100 = 60
        RIGHT_MASK  = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9) # 0b1111000000 = 960
        MIDDLE_MASK = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7) # 0b0011110000 = 240
        
        for mask in reserved_rows.values():
            left_free = (mask & LEFT_MASK) == 0
            right_free = (mask & RIGHT_MASK) == 0
            mid_free = (mask & MIDDLE_MASK) == 0
            
            if left_free and right_free:
                ans += 2
            elif left_free or right_free or mid_free:
                ans += 1
                
        return ans