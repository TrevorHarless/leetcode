"""
This is how far I got... but not quite. REVISIT.

"""

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        

        counts = [0, 0, 0] # counts for a,b,c

        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        for count in counts:
            if count < k:
                return -1

        # now that we have the counts

        # aabaaaacaabc
        #   l        r
        # [8, 2, 2]

        # 2
        # 11 - 3 = 8

        l, r = 0, len(s) - 1

        while l < r:
            # go until we cannot take either side and it be count > k

            if counts[ord(s[l]) - ord('a')] > k:
                l += 1
            elif counts[ord(s[r]) - ord('a')] > k:
                r -= 1
            else:
                # cannot take
                return r - l - 1
        
        return -1