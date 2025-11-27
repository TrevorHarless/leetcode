"""
1) 
Good refresher on Tries:
- TrieNodes contain 2 things, a hashmap children and a boolean endOfWord. 
The hashmap represents the children nodes with char to TrieNode. The boolean
indicates if that node is the end of a word -- helpful for searches

2) I missed how the search would work. I got very close but wasn't sure how to setup
the recursive call when the character we are checking is the "." char. Since its a ".",
this means we could have any of the possible paths at the current TrieNode or current level.

If you ever see a ".", you would need to recurse through each possible TrieNode at that
level in the Trie. The trick here is that we need to keep track of what character we are at
in the word we are searching for -- so then when we iterate through each character we 
start at the new index.

Then at the very end we are returning whether we are at the end of a word or not. If we
were able to successfully make it to the end of a path then that means the word exists.

3) Main thing here is parameters for the dfs call in this instance.


"""

class TrieNode:
    def __init__(self):
        self.children = {} # letter : TrieNode
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr_children = curr.children
            if c in curr_children:
                # found in hashmap
                curr = curr.children[c]

            else:
                # not found in children, add
                curr_children[c] = TrieNode()
                curr = curr.children[c]
        
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord

        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)