"""
1) When you are given time complexity constraints, brain storm the data structures 
that comply with those constraints. In this instance, hashmap and array alone complied with most
of the constraints but not all, therefore needed to be used in conjunction.
2) I initially was too focused on using a set because the problem is designing a set.
3) Refer to #1. 

"""

import random
class RandomizedSet:

    def __init__(self):
        # we have to use either:
        # 1) Hashmap
        # 2) Array (amortized O(1))   
        self.hm = {} # val : idx in arr
        self.arr = [] # val
        

    def insert(self, val: int) -> bool: 
        # hm --> insert the element
        # arr --> insert at the end
        if val in self.hm:
            return False

        self.arr.append(val)
        self.hm[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        # hm --> remove the element
        # arr --> we dont know where that element is, we cant
        if val not in self.hm:
            return False

        idx = self.hm[val]
        del self.hm[val]

        tmp = self.arr.pop()

        if val != tmp:
            self.arr[idx] = tmp
            self.hm[self.arr[idx]] = idx
        
        return True

    def getRandom(self) -> int:
        # hm --> get a list of the vals and choose random from idx's
        # arr --> choose random idx from 0 to len
        return self.arr[random.randint(0, len(self.arr) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()