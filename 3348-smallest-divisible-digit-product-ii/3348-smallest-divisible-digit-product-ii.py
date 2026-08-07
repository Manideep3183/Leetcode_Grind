class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        # Step 1: Factorize t into prime factors 2, 3, 5, 7
        req = [0, 0, 0, 0]  # count for 2, 3, 5, 7
        primes = [2, 3, 5, 7]
        temp_t = t
        for idx, p in enumerate(primes):
            while temp_t % p == 0:
                req[idx] += 1
                temp_t //= p
        
        # If t has prime factors other than 2, 3, 5, 7, it's impossible
        if temp_t > 1:
            return "-1"

        # Prime factor count mapping for digits 1..9
        digit_factors = {
            1: [0, 0, 0, 0],
            2: [1, 0, 0, 0],
            3: [0, 1, 0, 0],
            4: [2, 0, 0, 0],
            5: [0, 0, 1, 0],
            6: [1, 1, 0, 0],
            7: [0, 0, 0, 1],
            8: [3, 0, 0, 0],
            9: [0, 2, 0, 0],
        }

        def min_digits_needed(c2, c3, c5, c7):
            """Returns the minimum number of digits needed to supply required factors."""
            c2 = max(0, c2)
            c3 = max(0, c3)
            cnt5 = max(0, c5)
            cnt7 = max(0, c7)
            
            # Combine 3s into 9s, 2s into 8s
            cnt9 = c3 // 2
            rem3 = c3 % 2
            cnt8 = c2 // 3
            rem2 = c2 % 3
            
            cnt6 = 0
            cnt4 = 0
            
            if rem3 == 1 and rem2 == 1:
                cnt6 = 1
                rem3, rem2 = 0, 0
            elif rem3 == 1 and rem2 == 2:
                cnt6 = 1
                rem2 = 1
                rem3 = 0
            
            if rem2 == 2:
                cnt4 = 1
                rem2 = 0
                
            return cnt7 + cnt5 + cnt9 + cnt8 + cnt6 + cnt4 + rem3 + rem2

        def can_fit(rem_len, c2, c3, c5, c7):
            return min_digits_needed(c2, c3, c5, c7) <= rem_len

        n = len(num)
        
        # Find position of first '0' in num
        first_zero = num.find('0')
        if first_zero == -1:
            first_zero = n

        # Check if num itself is valid
        if first_zero == n:
            curr_factors = [0, 0, 0, 0]
            for ch in num:
                d = int(ch)
                for k in range(4):
                    curr_factors[k] += digit_factors[d][k]
            if all(curr_factors[k] >= req[k] for k in range(4)):
                return num

        # Precompute prefix factors of num up to first_zero
        prefix_factors = [[0]*4 for _ in range(n + 1)]
        for i in range(first_zero):
            d = int(num[i])
            for k in range(4):
                prefix_factors[i+1][k] = prefix_factors[i][k] + digit_factors[d][k]

        # Try to match prefix of length i (from first_zero down to 0)
        best_i = -1
        best_d = -1

        for i in range(first_zero, -1, -1):
            if i == n:
                continue
            
            start_d = int(num[i]) + 1 if i < n else 1
            for d in range(start_d, 10):
                rem_len = n - 1 - i
                needed = [req[k] - prefix_factors[i][k] - digit_factors[d][k] for k in range(4)]
                if can_fit(rem_len, *needed):
                    best_i = i
                    best_d = d
                    break
            if best_i != -1:
                break

        # Case 1: Solution exists with same length `n`
        if best_i != -1:
            res = list(num[:best_i]) + [str(best_d)]
            curr_req = [req[k] - prefix_factors[best_i][k] - digit_factors[best_d][k] for k in range(4)]
            
            # Greedily construct suffix
            for j in range(best_i + 1, n):
                rem_len = n - 1 - j
                for d in range(1, 10):
                    next_req = [curr_req[k] - digit_factors[d][k] for k in range(4)]
                    if can_fit(rem_len, *next_req):
                        res.append(str(d))
                        curr_req = next_req
                        break
            return "".join(res)

        # Case 2: Solution requires length > n
        min_len = min_digits_needed(*req)
        target_len = max(n + 1, min_len)
        
        res = []
        curr_req = list(req)
        for j in range(target_len):
            rem_len = target_len - 1 - j
            for d in range(1, 10):
                next_req = [curr_req[k] - digit_factors[d][k] for k in range(4)]
                if can_fit(rem_len, *next_req):
                    res.append(str(d))
                    curr_req = next_req
                    break

        return "".join(res)