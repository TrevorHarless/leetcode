"""
1) Notice the time constraint therefore get rid of sorting and think one-pass.
Use hashset for O(1) retrieval
2) N/A
3) N/A

Did great on this one. 

"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # cannot use sorting

        set_nums = set(nums)

        longest = 0
        for num in set_nums:

            # need to check if this is the start of a sequence
            if (num - 1) not in set_nums:
                # check for run
                current_run = 1
                
                while (num + current_run) in set_nums:
                    current_run += 1
                    
                longest = max(current_run, longest)
        
        return longest