"""
1) Learned to ensure variable naming is something I can remember, in the beginning 
I was using variables i, fast, and end, which didn't make much sense. Changed that to
write, accum, and current which allowed me to keep track of them better.

2) My edge case handling could have been simplified to the following:
chars[write_ptr] = current_char
write_ptr += 1
if count > 1:
    for c in str(count):
        chars[write_ptr] = c
        write_ptr += 1

Much cleaner. Notice the repeated work done in my edge case handling

3) See #1, no additional techniques could have been used here.
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        write_ptr = 0
        accum_ptr = 0
        current_ptr = 0

        while current_ptr < len(chars):

            current_char = chars[current_ptr]
            
            while accum_ptr < len(chars) and chars[accum_ptr] == current_char:
                accum_ptr += 1
            
            count = accum_ptr - current_ptr

            if count == 1: # only write char 
                chars[write_ptr] = current_char 
                write_ptr += 1 
            elif count < 10: 
                chars[write_ptr] = current_char 
                chars[write_ptr + 1] = str(count) 
                write_ptr += 2 
            else: 
                chars[write_ptr] = current_char 
                write_ptr += 1 
                count_char = str(count) 
                for c in enumerate(count_char): 
                    chars[write_ptr] = str(c)
                    write_ptr += 1 

            current_ptr = accum_ptr
                

        return write_ptr
        