import bisect

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        total_ones = s.count('1')
        
        # Parse all consecutive character segments in s
        segments = []  # List of (char, start, end)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            segments.append((s[i], i, j - 1))
            i = j
            
        # Extract '1'-segments and store their global segment index
        ones_segs = []
        for seg_idx, (char, start, end) in enumerate(segments):
            if char == '1':
                ones_segs.append((start, end, seg_idx))
                
        num_ones_segs = len(ones_segs)
        ones_starts = [seg[0] for seg in ones_segs]
        
        # Precompute static gain W[i] for internal '1'-segments
        W = [0] * num_ones_segs
        for i in range(num_ones_segs):
            _, _, seg_idx = ones_segs[i]
            
            # Must have both left and right '0'-segments
            if seg_idx > 0 and seg_idx + 1 < len(segments):
                left_len = segments[seg_idx - 1][2] - segments[seg_idx - 1][1] + 1
                right_len = segments[seg_idx + 1][2] - segments[seg_idx + 1][1] + 1
                W[i] = left_len + right_len
            else:
                W[i] = 0
            
        # Build Sparse Table for Range Maximum Query on W
        if num_ones_segs > 0:
            LOG = num_ones_segs.bit_length()
            st = [[0] * num_ones_segs for _ in range(LOG)]
            st[0] = list(W)
            
            for j in range(1, LOG):
                length = 1 << (j - 1)
                for k in range(num_ones_segs - (1 << j) + 1):
                    st[j][k] = max(st[j - 1][k], st[j - 1][k + length])
                    
            def query_st(L, R):
                if L > R:
                    return 0
                j = (R - L + 1).bit_length() - 1
                return max(st[j][L], st[j][R - (1 << j) + 1])
        else:
            def query_st(L, R):
                return 0

        ans = []
        for l, r in queries:
            # Binary search for '1'-segments fully inside [l, r]
            first_i = bisect.bisect_left(ones_starts, l)
            
            last_candidate = bisect.bisect_right(ones_starts, r) - 1
            last_i = last_candidate
            while last_i >= first_i and ones_segs[last_i][1] > r:
                last_i -= 1
                
            if first_i > last_i:
                # No '1'-segment fully inside [l, r]
                ans.append(total_ones)
                continue
                
            def calc_gain(idx):
                start, end, seg_idx = ones_segs[idx]
                
                # Must have both left and right '0' segments in s
                if seg_idx == 0 or seg_idx == len(segments) - 1:
                    return 0
                    
                l_start, l_end = segments[seg_idx - 1][1], segments[seg_idx - 1][2]
                r_start, r_end = segments[seg_idx + 1][1], segments[seg_idx + 1][2]
                
                eff_l_start = max(l_start, l)
                eff_r_end = min(r_end, r)
                
                # Both surrounding '0' segments must be non-empty within [l, r]
                if eff_l_start > l_end or r_start > eff_r_end:
                    return 0
                    
                return (l_end - eff_l_start + 1) + (eff_r_end - r_start + 1)

            if first_i == last_i:
                max_gain = calc_gain(first_i)
            else:
                gain_first = calc_gain(first_i)
                gain_last = calc_gain(last_i)
                gain_mid = query_st(first_i + 1, last_i - 1)
                max_gain = max(gain_first, gain_last, gain_mid)
                
            ans.append(total_ones + max_gain)
            
        return ans