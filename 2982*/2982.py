"""
Solution is correct but runs into memory issues...

"""

class Solution:
    def maximumLength(self, s: str) -> int:
        # get all substrings and their frequencies, return highest freq if >= 3


        sub_freqs = defaultdict(int)

        for i in range(len(s)):
            substring = s[i]
            special_char = s[i]

            sub_freqs[substring] += 1

            for j in range(i+1, len(s)):
                if s[j] != special_char:
                    break

                substring += s[j]
                sub_freqs[substring] += 1
        
        # return highest freq if >= 3

        
        longest_substring = -1

        print(sub_freqs)

        for substring, freq in sub_freqs.items():
            if freq >= 3 and len(substring) > longest_substring:
                longest_substring = len(substring)
        return longest_substring



