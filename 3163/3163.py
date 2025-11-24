"""
1) Similar to 443 but easier, I didn't miss anything
2) N/A
3) N/A

"""

class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""


        accum = 0
        i = 0
        
        while accum < len(word):
            current_char = word[accum]

            while (accum < len(word) and 
                    word[accum] == current_char and
                    accum - i < 9):
                accum += 1
            
            count = accum - i
            comp += str(count)
            comp += current_char
            
            i = accum
        
        return comp