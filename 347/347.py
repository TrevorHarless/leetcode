"""
Honestly I got this so fast, key here is using the lambda to get an array of tuples
sorted by the value (frequency of num). 

Good practice. 
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap with val : freq
        
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        # sort freq map by values

        out = []
        for num, frequency in sorted(freq.items(), key=lambda x : x[1], reverse=True):
            if len(out) == k:
                break
            out.append(num)
        
        return out