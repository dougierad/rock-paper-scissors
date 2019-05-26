#History string matching strategy
#Look for a pattern of length 'pattern_length' of last characters of their_history.
#Find that pattern (not including those last characters) in their_history and 
#beat their throw that comes next.

import random

strategy_name = "Doug's wHaCk history string matching"

def move(my_history, their_history):
    my_move = 'r'
    pattern_length = 4
    
    #find pattern just prior to this last move
    if len(their_history) < pattern_length + 1:
        pattern_position = -1
    else:
        #use rfind(str, 1, -1) The -1 ignores the last character to force rfind to find another instance
        #of the str other than the last one in the string
        pattern_position = their_history.rfind(their_history[-pattern_length : len(their_history)], 1, -1)

    if pattern_position == -1:
        #did not find a pattern, so throw random
        return random.choice(['r','p','s'])
    else:
        #found a pattern in the history, so beat the next throw after that pattern in the history
        their_next_after_pattern = their_history[pattern_position + pattern_length]
        if their_next_after_pattern == 'r':
            return 'p'
        elif their_next_after_pattern == 'p':
            return 's'
        elif their_next_after_pattern == 's':
            return 'r'
        else:
            return 'bad input'
            
    

