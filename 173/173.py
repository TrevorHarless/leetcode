"""
1) For this problem we are "flattening" out the BST into an array to allow us to iterate over
it in-order. 
2) N/A
3) N/A

Time: O(N) initialization and O(1) next and hasNext
Space: O(N) for the number of nodes

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def in_order(self, node):
        if not node:
            return
        
        self.in_order(node.left)
        # process
        self.nums.append(node.val)
        self.in_order(node.right)
        return


    def __init__(self, root: Optional[TreeNode]):
        # could we just build an array from the tree?
        self.nums = []
        self.in_order(root)
        self.pointer = -1

    def next(self) -> int:
        self.pointer += 1
        return self.nums[self.pointer]

    def hasNext(self) -> bool:
        return (self.pointer + 1) < len(self.nums)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()