class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime Factorization of t
        temp_t = t
        counts = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                counts[p] += 1
                temp_t //= p
        
        if temp_t > 1:
            return "-1"

        def get_min_digits(c2, c3, c5, c7):
            """
            Returns the minimal list of digits needed to fulfill 2^c2 * 3^c3 * 5^c5 * 7^c7.
            We want minimum number of digits, sorted ascending.
            """
            best_digits = None
            
            # c5 and c7 can only be represented by 5 and 7
            base = ['5'] * c5 + ['7'] * c7
            
            # Brute force / Search optimal combinations of 2 and 3 into digits {2,3,4,6,8,9}
            # c2 <= 50, c3 <= 50 in typical bounds, but we can do a quick check
            # For 3s: try using '9's as much as possible, then remaining '3' or combine with '2' into '6'
            # To minimize length:
            for d9 in range(c3 // 2, -1, -1):
                rem_c3 = c3 - d9 * 2
                for d8 in range(c2 // 3, -1, -1):
                    rem_c2 = c2 - d8 * 3
                    
                    # Try combining remaining 2 and 3 into 6
                    d6 = min(rem_c2, rem_c3)
                    rc2 = rem_c2 - d6
                    rc3 = rem_c3 - d6
                    
                    d4 = rc2 // 2
                    d2 = rc2 % 2
                    d3 = rc3
                    
                    digits = base + ['2']*d2 + ['3']*d3 + ['4']*d4 + ['6']*d6 + ['8']*d8 + ['9']*d9
                    if best_digits is None or len(digits) < len(best_digits) or (len(digits) == len(best_digits) and digits < best_digits):
                        digits.sort()
                        best_digits = digits
                        
            return "".join(best_digits) if best_digits else ""

        n = len(num)

        # Helper to compute factor counts of a single digit
        def get_factors(d):
            f = {2: 0, 3: 0, 5: 0, 7: 0}
            if d == 2: f[2] = 1
            elif d == 3: f[3] = 1
            elif d == 4: f[2] = 2
            elif d == 5: f[5] = 1
            elif d == 6: f[2] = 1; f[3] = 1
            elif d == 7: f[7] = 1
            elif d == 8: f[2] = 3
            elif d == 9: f[3] = 2
            return f

        # Handle '0' in `num`
        first_zero = num.find('0')
        if first_zero != -1:
            # We must change position at first_zero or earlier
            limit = first_zero
            
            # Precompute prefix counts up to limit
            pref = {2: 0, 3: 0, 5: 0, 7: 0}
            pref_at = [dict(pref)]
            for i in range(limit):
                f = get_factors(int(num[i]))
                for p in pref: pref[p] += f[p]
                pref_at.append(dict(pref))

            for i in range(limit, -1, -1):
                start_digit = int(num[i]) + 1 if i < limit else 1
                for d in range(start_digit, 10):
                    f = get_factors(d)
                    req2 = max(0, counts[2] - pref_at[i][2] - f[2])
                    req3 = max(0, counts[3] - pref_at[i][3] - f[3])
                    req5 = max(0, counts[5] - pref_at[i][5] - f[5])
                    req7 = max(0, counts[7] - pref_at[i][7] - f[7])

                    min_str = get_min_digits(req2, req3, req5, req7)
                    rem_len = n - 1 - i
                    if len(min_str) <= rem_len:
                        padding = '1' * (rem_len - len(min_str))
                        return num[:i] + str(d) + padding + min_str

            min_str = get_min_digits(counts[2], counts[3], counts[5], counts[7])
            return '1' * (n + 1 - len(min_str)) + min_str

        # Check if num itself is valid (no zero and product divisible by t)
        pref = {2: 0, 3: 0, 5: 0, 7: 0}
        pref_at = [dict(pref)]
        for i in range(n):
            f = get_factors(int(num[i]))
            for p in pref: pref[p] += f[p]
            pref_at.append(dict(pref))

        if all(pref[p] >= counts[p] for p in [2, 3, 5, 7]):
            return num

        # Backtrack from right to left to find pivot
        for i in range(n - 1, -1, -1):
            curr_digit = int(num[i])
            for d in range(curr_digit + 1, 10):
                f = get_factors(d)
                req2 = max(0, counts[2] - pref_at[i][2] - f[2])
                req3 = max(0, counts[3] - pref_at[i][3] - f[3])
                req5 = max(0, counts[5] - pref_at[i][5] - f[5])
                req7 = max(0, counts[7] - pref_at[i][7] - f[7])

                min_str = get_min_digits(req2, req3, req5, req7)
                rem_len = n - 1 - i
                if len(min_str) <= rem_len:
                    padding = '1' * (rem_len - len(min_str))
                    return num[:i] + str(d) + padding + min_str

        # Extend length by 1
        min_str = get_min_digits(counts[2], counts[3], counts[5], counts[7])
        return '1' * (n + 1 - len(min_str)) + min_str