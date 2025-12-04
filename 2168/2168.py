"""
For this problem the main thing I missed was creating a copy of the freq map in the helper
equaldigitfreq. I was using popitem which modified the original map.
"""

class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        
        result = set()

        def equalDigitFreq(freq) -> bool:
            freq_map = dict(freq)
            key, value = freq_map.popitem()
            
            for letter, count in freq_map.items():
                if count != value:
                    return False
            
            return True
        
        for i in range(len(s)):
            substring = s[i]
            freq = defaultdict(int)
            freq[s[i]] += 1

            result.add(substring)
            
            for j in range(i+1, len(s)):
                substring += s[j]
                freq[s[j]] += 1
                # if substring has equal digit freq, add it
                if equalDigitFreq(freq):
                    result.add(substring)

        return len(result)