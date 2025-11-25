"""
1) Had an almost correct approach with prefix/postfix product arrays but that isn't quite correct.
For these types of problems really need to analyze input and run through test cases with my 
potential solution.
2) I missed the idea of using left and right instead of pre and post. By using left and right you
can simply get the product of everything to the left and everything to the right. Don't overcomplicate.
3) N/A

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        [1,2,3,4]

        left and right product

        out --> [24, 12, 8, 6]

        start [1,2,3,4]
        left [1, 1, 2, 6] for each element its nums[i-1] * left[i-1]
        right [24,12,4,1] for each element in reverse its nums[i+1] * right[i+1]

        output [dummy * 24, 1 * 12, 2 * 4, 6 * dummy]
        """

        left = [0] * len(nums)
        right = [0] * len(nums)

        left[0] = 1       
        
        # Build left
        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]
        
        
        # Build right
        right[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        
        
        print(left)
        print(right)
        
        out = []

        for i in range(len(nums)):
            val = left[i] * right[i]
            out.append(val)
        return out